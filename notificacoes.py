import resend
import requests

from configs import EMAIL_REMETENTE, EMAIL_DESTINATARIOS, CONTA_ID, AUTH_TOKEN, RESEND_APIKEY
from twilio.rest import Client


def enviar_email(assunto, corpo):  
    try:
            resend.api_key = RESEND_APIKEY
            corpo_html = "<pre>" + corpo + "/pre"

            print("2 - conectando SMTP")
            print("API KEY:", resend.api_key)
            print("DESTINATARIOS:", EMAIL_DESTINATARIOS)
            print("ASSUNTO:", assunto)
            print("CORPO:", corpo)

            # envia para 2 emails
            for destinatario in EMAIL_DESTINATARIOS:

               r = resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": destinatario,
                "subject": assunto,
                "html": corpo_html
                })

            print(f"email enviado para {destinatario}")

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