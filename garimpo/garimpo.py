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
    if "captcha" in txt[:2000].lower():
        raise RuntimeError("bloqueada por captcha (Radware) fora do navegador")
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


def _slug_id(fonte, link):
    m = re.search(r"(\d{4,})(?:\D*$|\?)", link.split("?")[0])
    return f"{fonte.lower()}-{m.group(1) if m else re.sub(r'[^a-z0-9]+', '-', link.lower())[-50:]}"


def fonte_zuk():
    base = "https://www.portalzuk.com.br/leilao-de-imoveis/u/todos-imoveis/sp"
    out, vistos = [], set()
    for pag in range(1, 21):
        r = requests.get(base if pag == 1 else f"{base}?page={pag}", headers=UA, timeout=60)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        novos = 0
        for c in soup.select("div.card-property"):
            a = c.select_one(".card-property-image-wrapper a[href]")
            if not a or a["href"] in vistos:
                continue
            vistos.add(a["href"]); novos += 1
            tipo = (c.select_one(".card-property-price-lote") or a).get_text(" ", strip=True)
            end = c.select_one(".card-property-address")
            end_txt = end.get_text(" ", strip=True) if end else ""
            area = None
            for lab in c.select(".card-property-info-label"):
                m = re.search(r"([\d.,]+)\s*m", lab.get_text())
                if m and "terreno" not in lab.get_text():
                    area = num(m.group(1))
            precos, pct, data = [], None, None
            for li in c.select("li.card-property-price"):
                v = li.select_one(".card-property-price-value")
                if not v:
                    continue
                if v.find(style=re.compile("line-through")):
                    continue  # praça já passada
                vv = num(re.search(r"R\$\s*([\d.,]+)", v.get_text(" ")).group(1)) if re.search(r"R\$\s*([\d.,]+)", v.get_text(" ")) else None
                pp = li.select_one(".card-property-price-percent")
                if pp:
                    pct = num(pp.get_text())
                d = li.select_one(".card-property-price-data")
                if vv:
                    precos.append(vv); data = d.get_text(" ", strip=True) if d else data
            news = c.select_one(".card-property-news")
            out.append(dict(
                id=_slug_id("Zuk", a["href"]), fonte="Zuk", uf="SP", tipo=tipo,
                titulo=(a.get("title") or "").strip(), descricao=f"{tipo} {a.get('title') or ''} {news.get_text(strip=True) if news else ''}",
                cidade=end_txt.split("/")[0].strip() if "/" in end_txt else None,
                bairro=(end.select_one("span").get_text(" ", strip=True).split(" - ", 1)[-1] if end and end.select_one("span") else None),
                endereco=end_txt, area=area, lance_min=min(precos) if precos else None,
                desconto=pct, data_leilao=data, link=a["href"]))
        if novos == 0:
            break
    return out


def fonte_mega():
    base = "https://www.megaleiloes.com.br/imoveis/apartamentos/sp"
    out, vistos = [], set()
    for pag in range(1, 31):
        r = requests.get(base if pag == 1 else f"{base}?pagina={pag}", headers=UA, timeout=60)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        novos = 0
        for c in soup.select("div[data-key] div.card"):
            a = c.select_one("a.card-title[href]") or c.select_one("a.card-image[href]")
            if not a:
                continue
            link = a["href"].split("?")[0]
            if link in vistos:
                continue
            vistos.add(link); novos += 1
            titulo = a.get_text(" ", strip=True) or link.rsplit("/", 1)[-1].replace("-", " ")
            preco = c.select_one(".card-price")
            pct = c.select_one(".card-down .value")
            partes = link.split("/")
            cidade = partes[6].replace("-", " ").title() if len(partes) > 6 else None
            loc = c.select_one(".card-locality")
            area = re.search(r"-(\d+)-m2", link)
            out.append(dict(
                id=_slug_id("Mega", link), fonte="Mega", uf="SP", tipo="Apartamento", titulo=titulo,
                descricao=c.get_text(" ", strip=True)[:600], cidade=cidade,
                bairro=loc.get_text(" ", strip=True) if loc else None,
                area=num(area.group(1)) if area else None,
                lance_min=num(preco.get_text()) if preco else None,
                desconto=num(pct.get_text()) if pct else None, link=link))
        if novos == 0:
            break
    return out


FONTES = {"Caixa": fonte_caixa, "Zuk": fonte_zuk, "Mega": fonte_mega}


# ---------------- Supabase ----------------

def gravar(lotes, rodada):
    url, key = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY")
    if not url or not key:
        print("[modo teste] sem credenciais do Supabase; nada gravado.")
        return
    h = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
         "Prefer": "resolution=merge-duplicates,return=minimal"}
    cols = ["id", "fonte", "codigo", "uf", "cidade", "bairro", "endereco", "tipo", "titulo",
            "descricao", "modalidade", "data_leilao", "lance_min", "avaliacao", "desconto", "area",
            "dorm", "link", "rodada", "visto_em"]  # status fica com o Claude
    lotes = [{c: l.get(c) for c in cols} for l in lotes]
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
            rodada["fontes_fora"].append(f"{nome}: {e}"[:200])
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
                l.update(rodada=HOJE, visto_em=agora)
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
