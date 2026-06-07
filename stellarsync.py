import os
os.system("cls")

def exibir_menu():
    print("\n" + "=" * 50)
    print("       STELLAR SYNC — Gestão de Tráfego Orbital")
    print("=" * 50)
    print("  1. Sobre o sistema")
    print("  2. Cadastrar objeto orbital")
    print("  3. Simular trajetória e detectar colisão")
    print("  4. Recomendar manobra de desvio")
    print("  5. Gerar relatório de risco")
    print("  0. Sair")
    print("=" * 50)

def sobre_sistema():
    print("\n" + "-" * 50)
    print("  SOBRE O STELLAR SYNC")
    print("-" * 50)
    print(f""" O Stellar Sync é um sistema de gestão de tráfego
    orbital que monitora satélites e detritos espaciais.
    Detecta riscos de colisão e recomenda manobras
    coordenadas para evitar acidentes e reduzir o
    desperdício de combustível nas operações espaciais
    """)
    print("-" * 50)
    input("\n  Pressione ENTER para voltar ao menu...")

# Lista global que armazena todos os objetos orbitais cadastrados
objetos_orbitais = []

def cadastrar_objeto(objetos):
    print("\n" + "-" * 50)
    print("CADASTRAR OBJETO ORBITAL")
    print("-" * 50)

    # Nome
    while True:
        nome = input("Nome do objeto (ex: SAT-01, DETRITO-A): ").strip().upper()
        if nome:
            break
        print("Nome não pode ser vazio.")

    # Tipo com match-case
    print("Tipos disponíveis: 1 - Satélite Ativo  |  2 - Detrito  |  3 - Satélite Inativo")
    while True:
        tipo_opcao = input("Escolha o tipo (1/2/3): ").strip()
        match tipo_opcao:
            case "1":
                tipo = "Satélite Ativo"
                break
            case "2":
                tipo = "Detrito"
                break
            case "3":
                tipo = "Satélite Inativo"
                break
            case _:
                print("Opção inválida. Digite 1, 2 ou 3.")

    # Altitude
    while True:
        try:
            altitude = float(input("Altitude orbital (km, entre 160 e 2000): "))
            if 160 <= altitude <= 2000:
                break
            print("Altitude deve estar entre 160 km e 2000 km.")
        except ValueError:
            print("Digite um número válido.")

    # Velocidade
    while True:
        try:
            velocidade = float(input("Velocidade orbital (km/s, entre 6 e 10): "))
            if 6 <= velocidade <= 10:
                break
            print("Velocidade deve estar entre 6 e 10 km/s.")
        except ValueError:
            print("Digite um número válido.")

    # Monta o objeto como dicionário e adiciona à lista
    objeto = {
        "id": len(objetos) + 1,
        "nome": nome,
        "tipo": tipo,
        "altitude_km": altitude,
        "velocidade_kms": velocidade
    }
    objetos.append(objeto)

    print("\nObjeto cadastrado com sucesso!")
    print(f"     ID       : {objeto['id']}")
    print(f"     Nome     : {objeto['nome']}")
    print(f"     Tipo     : {objeto['tipo']}")
    print(f"     Altitude : {objeto['altitude_km']} km")
    print(f"     Velocidade: {objeto['velocidade_kms']} km/s")
    print("-" * 50)
    input("\n  Pressione ENTER para voltar ao menu...")

    return objetos

def classificar_risco(distancia):
    if distancia < 10:
        return "CRÍTICO"
    elif distancia < 50:
        return "MÉDIO"
    else:
        return "BAIXO"


def simular_trajetoria(objetos):
    print("\n" + "-" * 50)
    print("  SIMULAR TRAJETÓRIA E DETECTAR COLISÃO")
    print("-" * 50)

    # Verifica se há objetos suficientes
    if len(objetos) < 2:
        print("É necessário cadastrar ao menos 2 objetos para simular.")
        print("Vá ao menu e use a opção 2 para cadastrar.")
        input("\nPressione ENTER para voltar ao menu...")
        return

    print(f"{len(objetos)} objetos encontrados. Analisando pares...\n")

    encontrou_risco = False

    # Percorre todos os pares de objetos
    for i in range(len(objetos)):
        for j in range(i + 1, len(objetos)):
            obj_a = objetos[i]
            obj_b = objetos[j]

            # Calcula distância de altitude entre os dois objetos
            distancia = abs(obj_a["altitude_km"] - obj_b["altitude_km"])
            risco = classificar_risco(distancia)

            print(f"Par analisado: {obj_a['nome']} x {obj_b['nome']}")
            print(f"Altitude {obj_a['nome']}: {obj_a['altitude_km']} km")
            print(f"Altitude {obj_b['nome']}: {obj_b['altitude_km']} km")
            print(f"Distância entre objetos : {distancia:.1f} km")
            print(f"Nível de risco          : {risco}")
            print()

            if risco == "CRÍTICO":
                encontrou_risco = True

    if encontrou_risco:
        print("ATENÇÃO: Há pares em risco CRÍTICO!")
        print("Use a opção 4 para recomendar manobras de desvio.")
    else:
        print("Nenhum par em risco crítico no momento.")

    print("-" * 50)
    input("\n  Pressione ENTER para voltar ao menu...")

def recomendar_manobra(objetos):
    print("\n" + "-" * 50)
    print("  RECOMENDAR MANOBRA DE DESVIO")
    print("-" * 50)

    if len(objetos) < 2:
        print("É necessário ao menos 2 objetos cadastrados.")
        print("Use a opção 2 para cadastrar objetos.")
        input("\n  Pressione ENTER para voltar ao menu...")
        return

    pares_criticos = []

    # Encontra todos os pares em risco crítico
    for i in range(len(objetos)):
        for j in range(i + 1, len(objetos)):
            obj_a = objetos[i]
            obj_b = objetos[j]
            distancia = abs(obj_a["altitude_km"] - obj_b["altitude_km"])

            if distancia < 10:
                pares_criticos.append((obj_a, obj_b, distancia))

    if not pares_criticos:
        print("Nenhum par em risco crítico encontrado.")
        print("Nenhuma manobra necessária no momento.")
        input("\n  Pressione ENTER para voltar ao menu...")
        return

    print(f"  {len(pares_criticos)} par(es) em risco crítico. Gerando recomendações...\n")

    for idx, (obj_a, obj_b, distancia) in enumerate(pares_criticos, 1):
        print(f"  {'─' * 46}")
        print(f"  Ocorrência {idx}: {obj_a['nome']} x {obj_b['nome']}")
        print(f"  Distância atual: {distancia:.1f} km  |  Risco: CRÍTICO")
        print()

        # Define qual objeto deve desviar (prioriza satélite ativo)
        # Se ambos forem do mesmo tipo, desvia o de maior altitude
        match (obj_a["tipo"], obj_b["tipo"]):
            case ("Satélite Ativo", "Detrito") | ("Satélite Ativo", "Satélite Inativo"):
                objeto_desvia = obj_a
                objeto_fixo   = obj_b
            case ("Detrito", "Satélite Ativo") | ("Satélite Inativo", "Satélite Ativo"):
                objeto_desvia = obj_b
                objeto_fixo   = obj_a
            case _:
                # Ambos do mesmo tipo: desvia o de maior altitude
                objeto_desvia = obj_a if obj_a["altitude_km"] >= obj_b["altitude_km"] else obj_b
                objeto_fixo   = obj_b if objeto_desvia == obj_a else obj_a

        # Calcula nova altitude segura (desvio de 20 km acima do fixo)
        delta = 20.0
        nova_altitude = objeto_fixo["altitude_km"] + delta
        combustivel   = calcular_combustivel(delta)

        print(f"  Objeto a desviar : {objeto_desvia['nome']} ({objeto_desvia['tipo']})")
        print(f"  Objeto fixo      : {objeto_fixo['nome']} ({objeto_fixo['tipo']})")
        print(f"  Altitude atual   : {objeto_desvia['altitude_km']} km")
        print(f"  Nova altitude    : {nova_altitude:.1f} km  (+{delta} km acima do objeto fixo)")
        print(f"  Combustível est. : {combustivel} kg")
        print(f"  Direção          : Elevar órbita")
        print()

    print("Recomenda-se executar as manobras em até 24h.")
    print("-" * 50)
    input("\n  Pressione ENTER para voltar ao menu...")

# SISTEMA PRINCIPAL
def main():
    global objetos_orbitais
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                sobre_sistema()
            case "2":
                objetos_orbitais = cadastrar_objeto(objetos_orbitais)
            case "3":
                simular_trajetoria(objetos_orbitais)
            case "4":
                recomendar_manobra(objetos_orbitais)
            case "5":
                print("\n[em breve] Gerar relatório")
            case "0":
                print("\nEncerrando o Stellar Sync. Até logo!")
                break
            case _:
                print("\nOpção inválida. Digite um número entre 0 e 5.")


if __name__ == "__main__":
    main()