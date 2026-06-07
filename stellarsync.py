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

# SISTEMA PRINCIPAL
def main():
    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        match opcao:
            case "1":
                sobre_sistema()
            case "2":
                print("\n[em breve] Cadastrar objeto orbital")
            case "3":
                print("\n[em breve] Simular trajetória")
            case "4":
                print("\n[em breve] Recomendar manobra")
            case "5":
                print("\n[em breve] Gerar relatório")
            case "0":
                print("\n  Encerrando o Stellar Sync. Até logo!")
                break
            case _:
                print("\n  Opção inválida. Digite um número entre 0 e 5.")


if __name__ == "__main__":
    main()