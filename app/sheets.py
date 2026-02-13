import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

load_dotenv()

def salvar_no_sheets(dados):

    scope = ["https://www.googleapis.com/auth/spreadsheets"]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(os.getenv("GOOGLE_SHEET_NAME")).worksheet(
        os.getenv("GOOGLE_WORKSHEET")
    )

    sheet.clear()

    sheet.append_row([
        "Código","Produto","Estoque",
        "Preço","Pesagem Pacote","Pesagem Caixa"
    ])

    sheet.append_rows(dados)
