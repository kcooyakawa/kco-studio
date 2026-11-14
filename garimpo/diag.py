import requests, re
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36","Accept-Language":"pt-BR,pt;q=0.9","Accept":"text/html,application/xhtml+xml,*/*"}
for u in ["https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.csv","https://www.portalzuk.com.br/leilao-de-imoveis/u/todos-imoveis/sp","https://www.megaleiloes.com.br/imoveis/apartamentos/sp","https://www.sodresantoro.com.br","https://www.frazaoleiloes.com.br"]:
    try:
        r=requests.get(u,headers=UA,timeout=40)
        t=r.text
        print("=="*5,u,r.status_code,len(r.content),r.headers.get("server"),r.headers.get("content-type"))
        print(re.sub(r"\s+"," ",t[:600]))
        print("hrefs:",re.findall(r'href="([^"]{10,120})"',t)[:25])
    except Exception as e: print(u,"ERR",e)
