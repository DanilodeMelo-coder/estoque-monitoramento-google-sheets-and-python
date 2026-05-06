import os
from dotenv import load_dotenv

load_dotenv()

PLANILHA_ID = os.getenv("PLANILHA_ID")
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_DESTINATARIOS = [e.strip() for e in os.getenv("EMAIL_DESTINATARIOS").split(",")]
SENHA_APP = os.getenv("SENHA_APP")


ABA_NOME = "Cadastro_Produto"
COLUNA_PRODUTO = 2
COLUNA_ESTOQUE = 3
LINHA_INICIO = 4


LIMITE_ATENCAO  = 20      
LIMITE_URGENTE  = 15        
LIMITE_CRITICO  = 10 
LIMITE_ULTRA_CRITICO = 5



INTERVALO_HORAS = 1