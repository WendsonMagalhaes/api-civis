import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def extrair_tabela():
    session = requests.Session()
    login_url = "https://distribuidoraesperanca.civis.com.br/autenticacao"
    session.get(login_url)

    payload = {
        "data[Usuario][login]": os.getenv("CIVIS_USER"),
        "data[Usuario][senha]": os.getenv("CIVIS_PASSWORD")
    }

    response = session.post(login_url, data=payload)
    if response.status_code != 200:
        raise Exception("Falha no login, verifique usuário e senha")

    url_painel = "https://distribuidoraesperanca.civis.com.br/"
    pagina = session.get(url_painel)
    soup = BeautifulSoup(pagina.text, "html.parser")
    tabela = soup.find("table", class_="table-lista")

    if not tabela:
        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(pagina.text)
        raise Exception("Tabela não encontrada. Verifique debug.html")

    linhas = tabela.find("tbody").find_all("tr")
    dados = []

    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) == 6:
            dados.append([colunas[i].get_text(strip=True) for i in range(6)])

    return dados
