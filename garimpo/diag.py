import requests, re
UA={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36","Accept-Language":"pt-BR,pt;q=0.9","Accept":"text/html,application/xhtml+xml,*/*"}
for u in ["https://www.portalzuk.com.br/leilao-de-imoveis/u/todos-imoveis/sp","https://www.megaleiloes.com.br/imoveis/apartamentos/sp"]:
    t=requests.get(u,headers=UA,timeout=40).text
    print("==========",u, "R$ count:", t.count("R$"))
    for m in list(re.finditer(r"R\$", t))[:3]:
        print("----"); print(re.sub(r"\s+"," ",t[max(0,m.start()-2500):m.start()+400]))
