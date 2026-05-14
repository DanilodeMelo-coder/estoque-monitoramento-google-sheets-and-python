import gspread
from google.oauth2.service_account import Credentials
from configs import PLANILHA_ID, ABA_NOME, COLUNA_PRODUTO, COLUNA_ESTOQUE, LINHA_INICIO
import json
import os

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]

def pegar_creds():
    creds_dict = json.loads(os.getenv("credenciais"))
    return creds = Credentials.from_service_account_file(creds_dict, scopes=SCOPES)

def ler_estoque():
    creds = pegar_creads()
    client = gspread.authorize(creds)

    planilha = client.open_by_key(PLANILHA_ID)
    aba = planilha.worksheet(ABA_NOME)
    dados = aba.get_all_values()

    produtos = []
    for linha in dados[LINHA_INICIO:]:
        produto = linha[COLUNA_PRODUTO].strip()
        estoque_raw = linha[COLUNA_ESTOQUE].strip()

        if not produto or not estoque_raw:
            continue

        try:
            estoque = int(estoque_raw)
            produtos.append({"produto": produto, "estoque": estoque})
        except ValueError:
            print(f"Ignorando linha inválida: {linha}")

    return produtos