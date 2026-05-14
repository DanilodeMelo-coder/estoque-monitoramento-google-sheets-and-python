import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configs import EMAIL_REMETENTE, EMAIL_DESTINATARIOS, SENHA_APP, CONTA_ID, AUTH_TOKEN
from twilio.rest import Client

def enviar_email(assunto, corpo):  
    try: 
        print("1 - antes do SMTP")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_REMETENTE, SENHA_APP)

        print("Conectando SMTP...")

        print("2 - após conexão")


        for destinatario in EMAIL_DESTINATARIOS:

            msg = MIMEMultipart()
            msg["From"] = EMAIL_REMETENTE
            msg["To"] = destinatario
            msg["Subject"] = assunto
            msg.attach(MIMEText(corpo, "plain", "utf-8"))

            
            server.send_message(msg)
            print("✅ E-mail enviado!")

     except Exception as e:
        print("❌ Erro no email:", e)

def enviar_whatsapp(mensagem):
    cliente = Client(CONTA_ID, AUTH_TOKEN)

    mensagem = cliente.messages.create(
     from_='whatsapp:+14155238886',
     body='Teste enviado pelo Python',
     to='whatsapp:+5511998113976'
    )

    print(mensagem.sid)

#    resp = requests.get(url, params=params)
#    if resp.status_code == 200:
#        print("✅ WhatsApp enviado!")
#    else:
#        print(f"❌ Erro WhatsApp: {resp.text}")