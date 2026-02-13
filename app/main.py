from app.civis import extrair_tabela
import pandas as pd

if __name__ == "__main__":
    dados = extrair_tabela()
    print("Total de linhas:", len(dados))

    df = pd.DataFrame(dados, columns=[
        "Código", "Produto", "Estoque", "Preço", "Pesagem Pacote", "Pesagem Caixa"
    ])

    print(df.head())
