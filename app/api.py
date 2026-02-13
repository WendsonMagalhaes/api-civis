from fastapi import APIRouter
from app.civis import extrair_tabela
import pandas as pd

router = APIRouter()

@router.get("/atualizar-estoque")
def atualizar_estoque():
    try:
        dados = extrair_tabela()
        df = pd.DataFrame(dados, columns=[
            "Código", "Produto", "Estoque", "Preço", "Pesagem Pacote", "Pesagem Caixa"
        ])

        # Limpeza do Preço
        df["Preço"] = (
            df["Preço"]
            .str.replace("R$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

        # Limpeza do Estoque
        df["Estoque"] = (
            df["Estoque"]
            .str.replace(" KG", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

        # Transformar em lista de dicionários para JSON
        resultado = df.to_dict(orient="records")
        return {"total": len(resultado), "dados": resultado}

    except Exception as e:
        return {"erro": str(e)}
