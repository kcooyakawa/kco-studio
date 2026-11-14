"""Robô de triagem do W3W Select Club.

Roda no GitHub Actions (sem depender de computador ligado e sem gastar crédito do Claude).
Baixa listagens de leilão, aplica os filtros duros e grava os candidatos no Supabase
(tabela garimpo_lotes). O Claude só entra depois, na due diligence dos que passaram.

Sem SUPABASE_URL/SUPABASE_SERVICE_KEY roda em modo teste (só imprime).
"""
import csv, io, json, os, re, sys, unicodedata
from datetime import datetime, timezone, timedelta
import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language": "pt-BR,pt;q=0.9"}
SP_TZ = timezone(timedelta(hours=-3))
HOJE = datetime.now(SP_TZ).strftime("%Y-%m-%d")

# ---- regras de triagem (ajuste aqui) ----
PRECO_MIN = 60_000          # lance mínimo
PRECO_MAX = 1_500_000       # com financiamento/parcelamento, capital ~30% cabe em R$ 500 mil
DESCONTO_MIN = 30.0         # % abaixo da avaliação (proxy; o mercado real o Claude confere)
TIPOS_OK = ("apartamento",)
PROIBIDOS = ["usufruto", "nua propriedade", "nua-propriedade", "direitos hereditarios",
             "direitos possessorios", "cessao de direitos", "direitos sobre", "fracao ideal",
             "parte ideal", "% do imovel", "invadido", "invasao", "usucapiao", "rural"]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s).strip().lower()


def num(s):
    s = re.sub(r"[^\d,.-]", "", s or "")
    if not s:
        return None
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"-?\d+\.\d{1,2}", s):
        pass  # "50.00" já é decimal
    else:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


def triar(l):
    """Devolve (status, motivo). status: candidato | descartado."""
    texto = norm(" ".join(str(l.get(k) or "") for k in ("tipo", "descricao", "titulo")))
    if l.get("uf") and l["uf"].upper() != "SP":
        return "descartado", "fora de SP"
    if not any(t in texto for t in TIPOS_OK):
        return "descartado", "não é apartamento"
    for p in PROIBIDOS:
        if p in texto:
            return "descartado", f"impeditivo: {p}"
    p = l.get("lance_min")
    if p is None:
        return "descartado", "sem preço"
    if p < PRECO_MIN or p > PRECO_MAX:
        return "descartado", "fora da faixa de preço"
    d = l.get("desconto")
    if d is not None and d < DESCONTO_MIN:
        return "descartado", f"desconto {d:.0f}% < {DESCONTO_MIN:.0f}%"
    return "candidato", None


# ---------------- fontes ----------------

def fonte_caixa():
    url = "https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.csv"
    r = requests.get(url, headers=UA, timeout=90)
    r.raise_for_status()
    txt = r.content.decode("latin-1")
    linhas = txt.splitlines()
    ini = next(i for i, x in enumerate(linhas) if "UF" in x and ";" in x)
    rd = csv.reader(io.StringIO("\n".join(linhas[ini:])), delimiter=";")
    cab = [norm(c) for c in next(rd)]
    def col(*nomes):
        for n in nomes:
            for i, c in enumerate(cab):
                if n in c:
                    return i
        return None
    ix = dict(id=col("n do imovel", "imovel"), uf=col("uf"), cidade=col("cidade"),
              bairro=col("bairro"), end=col("endereco"), preco=col("preco"),
              aval=col("avaliacao"), desc=col("desconto"), descr=col("descricao"),
              mod=col("modalidade"), link=col("link"))
    out = []
    for row in rd:
        if len(row) < len(cab) - 1:
            continue
        g = lambda k: row[ix[k]].strip() if ix[k] is not None and ix[k] < len(row) else ""
        descr = g("descr")
        area = re.search(r"([\d.,]+)\s*de area privativa", norm(descr))
        qtos = re.search(r"(\d+)\s*qto", norm(descr))
        cod = re.sub(r"\D", "", g("id"))
        out.append(dict(
            id=f"caixa-{cod}", fonte="Caixa", codigo=cod, uf=g("uf"), cidade=g("cidade").title(),
            bairro=g("bairro").title(), endereco=g("end"), tipo=descr.split(",")[0],
            descricao=descr, lance_min=num(g("preco")), avaliacao=num(g("aval")),
            desconto=num(g("desc")), modalidade=g("mod"),
            area=num(area.group(1)) if area else None,
            dorm=int(qtos.group(1)) if qtos else None, link=g("link")))
    return out


def _cards_genericos(fonte, base, html):
    """Extração genérica: JSON-LD + cartões com link de imóvel e preço."""
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
        except Exception:
            continue
        for it in data if isinstance(data, list) else [data]:
            if isinstance(it, dict) and it.get("url") and it.get("name"):
                preco = (it.get("offers") or {}).get("price") if isinstance(it.get("offers"), dict) else None
                out.append(dict(titulo=it["name"], link=it["url"], lance_min=num(str(preco or ""))))
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if not re.search(r"imovel|lote|leilao", h, re.I):
            continue
        card = a.find_parent(["div", "article", "li"]) or a
        t = card.get_text(" ", strip=True)
        m = re.findall(r"R\$\s*([\d.]+,\d{2})", t)
        if not m or len(t) < 30:
            continue
        link = h if h.startswith("http") else base.rstrip("/") + "/" + h.lstrip("/")
        out.append(dict(titulo=t[:300], link=link, lance_min=min(num(x) for x in m)))
    vistos, res = set(), []
    for o in out:
        if o["link"] in vistos:
            continue
        vistos.add(o["link"])
        cod = re.sub(r"[^a-z0-9]+", "-", o["link"].lower().split("//")[-1])[-60:].strip("-")
        o.update(id=f"{fonte.lower()}-{cod}", fonte=fonte, tipo=o["titulo"], descricao=o["titulo"], uf="SP")
        res.append(o)
    return res


def fonte_zuk():
    base = "https://www.portalzuk.com.br"
    r = requests.get(f"{base}/leilao-de-imoveis/u/todos-imoveis/sp", headers=UA, timeout=60)
    r.raise_for_status()
    return _cards_genericos("Zuk", base, r.text)


def fonte_mega():
    base = "https://www.megaleiloes.com.br"
    r = requests.get(f"{base}/imoveis/apartamentos/sp", headers=UA, timeout=60)
    r.raise_for_status()
    return _cards_genericos("Mega", base, r.text)


FONTES = {"Caixa": fonte_caixa, "Zuk": fonte_zuk, "Mega": fonte_mega}


# ---------------- Supabase ----------------

def gravar(lotes, rodada):
    url, key = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
    if not url or not key:
        print("[modo teste] sem credenciais do Supabase; nada gravado.")
        return
    h = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
         "Prefer": "resolution=merge-duplicates,return=minimal"}
    for i in range(0, len(lotes), 500):
        r = requests.post(f"{url}/rest/v1/garimpo_lotes?on_conflict=id", headers=h,
                          data=json.dumps(lotes[i:i + 500], default=str), timeout=60)
        if r.status_code >= 300:
            sys.exit(f"Erro gravando lotes: {r.status_code} {r.text[:500]}")
    r = requests.post(f"{url}/rest/v1/garimpo_rodadas?on_conflict=data", headers=h,
                      data=json.dumps(rodada, default=str), timeout=60)
    if r.status_code >= 300:
        sys.exit(f"Erro gravando rodada: {r.status_code} {r.text[:500]}")
    print(f"Gravados {len(lotes)} lotes no Supabase.")


def main():
    agora = datetime.now(timezone.utc).isoformat()
    rodada = dict(data=HOJE, fontes_ok=[], fontes_fora=[], triados=0, candidatos=0,
                  por_fonte={}, descartes={})
    gravaveis = []
    for nome, fn in FONTES.items():
        try:
            lotes = fn()
        except Exception as e:
            print(f"!! {nome}: {type(e).__name__}: {e}")
            rodada["fontes_fora"].append(f"{nome}: {type(e).__name__}")
            continue
        if not lotes:
            rodada["fontes_fora"].append(f"{nome}: nenhum lote extraído (layout mudou ou bloqueio)")
            print(f"!! {nome}: 0 lotes")
            continue
        rodada["fontes_ok"].append(nome)
        cand = 0
        for l in lotes:
            st, motivo = triar(l)
            rodada["triados"] += 1
            if st == "candidato":
                cand += 1
                l.update(status="candidato", motivo=None, rodada=HOJE, visto_em=agora)
                gravaveis.append(l)
            else:
                rodada["descartes"][motivo.split(":")[0]] = rodada["descartes"].get(motivo.split(":")[0], 0) + 1
        rodada["candidatos"] += cand
        rodada["por_fonte"][nome] = {"triados": len(lotes), "candidatos": cand}
        print(f"{nome}: {len(lotes)} triados, {cand} candidatos")
    gravaveis.sort(key=lambda x: -(x.get("desconto") or 0))
    for l in gravaveis[:15]:
        print(f"  {l['fonte']:5} {l.get('desconto') or 0:5.1f}%  R$ {l['lance_min']:>12,.0f}  "
              f"{l.get('bairro') or ''} {l.get('cidade') or ''}  {l['link']}")
    print(json.dumps(rodada, ensure_ascii=False, indent=1))
    gravar(gravaveis, rodada)
    if not rodada["fontes_ok"]:
        sys.exit("Nenhuma fonte funcionou.")


if __name__ == "__main__":
    main()
