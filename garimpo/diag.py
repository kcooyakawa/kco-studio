# diagnóstico manual: python garimpo/diag.py
import requests, re
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36","Accept-Language":"pt-BR,pt;q=0.9"}
for u in ["https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.csv","https://www.portalzuk.com.br/leilao-de-imoveis/u/todos-imoveis/sp","https://www.megaleiloes.com.br/imoveis/apartamentos/sp"]:
    r=requests.get(u,headers=UA,timeout=40)
    print(u, r.status_code, len(r.content), re.sub(r"\s+"," ",r.text[:300]))
