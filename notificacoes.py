import resend
import requests

from configs import EMAIL_REMETENTE, EMAIL_DESTINATARIO, CONTA_ID, AUTH_TOKEN, RESEND_APIKEY
from twilio.rest import Client


def enviar_email(assunto, corpo):  
    try:
            resend.api_key = RESEND_APIKEY
            corpo_html = "<pre>" + corpo + "/pre"

            #teste
            print("DESTINATARIOS:", EMAIL_DESTINATARIO)
            print("ASSUNTO:", assunto)
            print("CORPO:", corpo)

            # envia para 2 emails

            r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": EMAIL_DESTINATARIO,
            "subject": assunto,
            "html": corpo_html
            })

            print(f"email enviado para {EMAIL_DESTINATARIO}")

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