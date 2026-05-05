import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configs import EMAIL_REMETENTE, EMAIL_DESTINATARIO, SENHA_APP

def enviar_email(assunto, corpo):  

    msg = MIMEMultipart()
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINATARIO
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_REMETENTE, SENHA_APP)
        server.send_message(msg)
    print("✅ E-mail enviado!")

