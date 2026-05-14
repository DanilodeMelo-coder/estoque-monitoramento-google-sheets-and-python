import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

email = os.getenv("EMAIL_REMETENTE")
senha = os.getenv("SENHA_APP")

print("EMAIL:", email)
print("SENHA repr:", repr(senha))
print("TAMANHO:", len(senha))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.set_debuglevel(1)
        server.login(email, senha)

    print("LOGIN OK")

except Exception as e:
    print("ERRO:", e)