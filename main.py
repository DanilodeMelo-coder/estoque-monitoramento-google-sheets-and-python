import schedule
import time
from sheets import ler_estoque
from alertas import classificar, montar_email, montar_whatsapp
from notificacoes import enviar_email, enviar_whatsapp
from configs import INTERVALO_HORAS

def verificar():
    print("Verificando estoque...")
    try:
        produtos = ler_estoque()
        ultra_critico, critico, urgente, atencao, ok = classificar(produtos)

        print(f" Ultra_critico: {len(ultra_critico)} | Crítico: {len(critico)} |  Urgente: {len(urgente)} |  Atenção: {len(atencao)} |  OK: {len(ok)}")

        if not (ultra_critico or critico or urgente or atencao):
            print("   Estoque OK, nenhum alerta necessário.")
            return

        assunto, corpo = montar_email(ultra_critico, critico, urgente, atencao)
        msg_whats = montar_whatsapp(ultra_critico,critico, urgente, atencao)

        enviar_email(assunto, corpo)
        enviar_whatsapp(msg_whats)

    except Exception as e:
        print(f" Erro: {e}")


verificar()
schedule.every(INTERVALO_HORAS).hours.do(verificar)

print(f" Monitorando a cada {INTERVALO_HORAS}h... (Ctrl+C para parar)")
while True:
    schedule.run_pending()
    time.sleep(60)