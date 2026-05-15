import smtplib
import resend
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configs import EMAIL_REMETENTE, EMAIL_DESTINATARIOS, SENHA_APP, CONTA_ID, AUTH_TOKEN, REDEND_APIKEY
from twilio.rest import Client

def enviar_email(assunto, corpo):  
    try:
            print("2 - conectando SMTP")

            for destinatario in EMAIL_DESTINATARIOS:

               r = resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": destinatario,
                "subject": assunto,
                "html": "<p>email enviado para<strong>destinatario</strong>!</p>"
                })

            print("4 - conexão finalizada")

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