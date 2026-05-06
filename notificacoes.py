import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configs import EMAIL_REMETENTE, EMAIL_DESTINATARIOS, SENHA_APP

def enviar_email(assunto, corpo):  

    for destinatario in EMAIL_DESTINATARIOS:

        msg = MIMEMultipart()
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = destinatario
        msg["Subject"] = assunto
        msg.attach(MIMEText(corpo, "plain", "utf-8"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_REMETENTE, SENHA_APP)
            server.send_message(msg)
        print("✅ E-mail enviado!")

