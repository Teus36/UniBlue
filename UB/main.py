from utils import limpar_tela, esperar
from persistencia import carregar_arquivo

from estudantes import menu_estudantes
from gastos import menu_gastos
from contas import menu_contas
from relatorios import menu_relatorios


estudantes = carregar_arquivo("estudantes.dat")
gastos = carregar_arquivo("gastos.dat")
contas = carregar_arquivo("contas.dat")


def menu_principal():
    while True:
        limpar_tela()

        print("==" * 21)
        print("|  SISTEMA DE GESTÃO DESPESAS UNIBLUE    |")
        print("==" * 21)
        print("|  1. ESTUDANTES                         |")
        print("|  2. GASTOS                             |")
        print("|  3. CONTAS                             |")
        print("|  4. RELATÓRIOS                         |")
        print("|  5. SOBRE O SISTEMA                    |")
        print("|  6. SAIR                               |")
        print("==" * 21)

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            esperar()
            continue

        if opcao == 1:
            menu_estudantes(estudantes)

        elif opcao == 2:
            menu_gastos(gastos, estudantes)

        elif opcao == 3:
            menu_contas(contas)

        elif opcao == 4:
            menu_relatorios(estudantes, gastos, contas)

        elif opcao == 5:
            print("EM ANDAMENTO")
            esperar()

        elif opcao == 6:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")
            esperar()


menu_principal()