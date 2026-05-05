from configs import LIMITE_ATENCAO, LIMITE_URGENTE, LIMITE_CRITICO, LIMITE_ULTRA_CRITICO

def classificar(produtos):
    ultra_critico = []
    critico  = []
    urgente  = []
    atencao  = []
    ok       = []

    for p in produtos:
        e = p["estoque"]
        if e <= LIMITE_ULTRA_CRITICO:
            ultra_critico.append(p)
        elif e <= LIMITE_CRITICO:
            critico.append(p)
        elif e <= LIMITE_URGENTE:
            urgente.append(p)
        elif e <= LIMITE_ATENCAO:
            atencao.append(p)
        else:
            ok.append(p)

    return ultra_critico, critico, urgente, atencao, ok

def montar_email(ultra_critico, critico, urgente, atencao):
    if ultra_critico:
        assunto =f"ULTRA CRITICO, estoque minimo em {len(ultra_critico)} produtos"
    elif critico:
        assunto = f"CRÍTICO: {len(critico)} produto(s) com estoque abaixo da média!"
    elif urgente:
        assunto = f"URGENTE: Estoque baixo em {len(urgente)} produto(s)"
    else:
        assunto = f"ATENÇÃO: {len(atencao)} produto(s) precisam de reposição"

    corpo = "=== RELATÓRIO DE ESTOQUE ===\n\n"

    if ultra_critico:
        corpo += "-ULTRA CRÍTICO (≤ 5 un.) — COMPRA URGENTE:\n"
        for p in ultra_critico:
            corpo += f"  • {p['produto']}: {p['estoque']} un.\n"
        corpo += "\n"

    if critico:
        corpo += "-CRÍTICO (≤ 10 un.) — COMPRA IMEDIATA:\n"
        for p in critico:
            corpo += f"  • {p['produto']}: {p['estoque']} un.\n"
        corpo += "\n"

    if urgente:
        corpo += "-URGENTE (≤ 15 un.):\n"
        for p in urgente:
            corpo += f"  • {p['produto']}: {p['estoque']} un.\n"
        corpo += "\n"

    if atencao:
        corpo += "-ATENÇÃO (≤ 20 un.):\n"
        for p in atencao:
            corpo += f"  • {p['produto']}: {p['estoque']} un.\n"
        corpo += "\n"

    todos = critico + urgente + atencao
    corpo += "=== LISTA DE COMPRAS ===\n"
    for p in todos:
        if p["estoque"] <= 5:
            nivel = "ULTRA CRÍTICO"
        elif p["estoque"] <= 10:
            nivel = "CRÍTICO"
        elif p["estoque"] <= 15:
            nivel = "URGENTE"
        else:
            nivel = "ATENÇÃO"
        corpo += f"  {nivel} | {p['produto']} ({p['estoque']} un. restantes)\n"

    from datetime import datetime
    corpo += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    return assunto, corpo
