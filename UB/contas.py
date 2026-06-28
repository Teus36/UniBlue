
from utils import limpar_tela, continuar, esperar
from persistencia import salvar_arquivo, proximo_id


def cadastrar_conta(contas):
    limpar_tela()

    nome_c = input("Nome da conta: ")
    valor_c = float(input("Valor da conta: "))
    vencimento_c = input("Data de vencimento: ")

    id_conta = proximo_id(contas)

    contas[id_conta] = [
        nome_c,
        valor_c,
        vencimento_c,
        "PENDENTE",
        True
    ]

    salvar_arquivo("contas.dat", contas)

    print(f"Conta cadastrada com ID {id_conta}!")

    esperar()


def listar_contas(contas):
    limpar_tela()

    if not contas:
        print("Nenhuma conta cadastrada!")

    else:
        for id_c, dados in contas.items():

            if not dados[4]:
                continue

            print("=" * 42)
            print(f"| {'DADOS DA CONTA':^38} |")
            print("=" * 42)

            print(f"| ID: {str(id_c):<34} |")
            print(f"| Conta: {dados[0][:28]:<31} |")
            print(f"| Valor: R$ {str(dados[1]):<28} |")
            print(f"| Vencimento: {dados[2]:<26} |")
            print(f"| Situação: {dados[3]:<28} |")
            print(f"| Status: {'ATIVO':<30} |")

            print("=" * 42)

    continuar()

def atualizar_conta(contas):
    limpar_tela()

    id_att_c = str(input("Informe o ID da conta: "))

    if id_att_c in contas and contas[id_att_c][4]:

        print("==" * 21)
        print("|         ATUALIZAÇÃO DE CONTA           |")
        print("==" * 21)
        print("|  1. NOME DA CONTA                      |")
        print("|  2. VALOR                              |")
        print("|  3. VENCIMENTO                         |")
        print("|  4. ATUALIZAR TODOS OS DADOS           |")
        print("|  5. VOLTAR                             |")
        print("==" * 21)

        try:
            opcao_att_c = int(input("Qual informação deseja atualizar? "))
        except ValueError:
            print("Digite apenas números!")
            esperar()
            return

        if opcao_att_c == 1:
            contas[id_att_c][0] = input("Novo nome da conta: ")

        elif opcao_att_c == 2:
            contas[id_att_c][1] = float(input("Novo valor: "))

        elif opcao_att_c == 3:
            contas[id_att_c][2] = input("Novo vencimento: ")

        elif opcao_att_c == 4:

            nome_c = input("Nome da conta: ")
            valor_c = float(input("Valor: "))
            vencimento_c = input("Vencimento: ")

            situacao_c = contas[id_att_c][3]
            status_c = contas[id_att_c][4]

            contas[id_att_c] = [
                nome_c,
                valor_c,
                vencimento_c,
                situacao_c,
                status_c 
            ]

        elif opcao_att_c == 5:
            return
        
        else:
            print("Opção inválida!")
            esperar()
            return

        salvar_arquivo("contas.dat", contas)
        print("Conta atualizada com sucesso!")

    else:
        print("ID não encontrado!")

    esperar()

def deletar_conta(contas):
    limpar_tela()

    deletar_c = str(input("Informe o ID da conta: "))

    if deletar_c in contas and contas[deletar_c][4]:
        contas[deletar_c][4] = False

        salvar_arquivo("contas.dat", contas)

        print("Conta removida com sucesso!")
    else:
        print("ID não encontrado!")

    esperar()

def pagar_conta(contas):
    limpar_tela()

    id_pagar_c = str(input("Informe o ID da conta: "))

    if id_pagar_c not in contas or not contas[id_pagar_c][4]:
        print("ID não encontrado!")
    elif contas[id_pagar_c][3] == "PAGA":
        print("Essa conta já foi paga!")
    else:
        contas[id_pagar_c][3] = "PAGA"
        print("Conta marcada como paga!")

    salvar_arquivo("contas.dat", contas)

    esperar()


def menu_contas(contas): 
    while True:
            limpar_tela()

            print("==" * 21)
            print("|            MÓDULO DE CONTAS            |")
            print("==" * 21)
            print("|  1. CADASTRAR CONTA                    |")
            print("|  2. LISTAR CONTAS                      |")
            print("|  3. ATUALIZAR CONTA                    |")
            print("|  4. DELETAR CONTA                      |")
            print("|  5. MARCAR COMO PAGA                   |")
            print("|  6. VOLTAR                             |")
            print("==" * 21)
            print()

            try:
                opcao_c = int(input("Selecione uma das opções acima: "))
            except ValueError:
                print("Digite apenas números!")
                esperar()
                continue

            if opcao_c == 1:
                cadastrar_conta(contas)
            elif opcao_c == 2:
                listar_contas(contas)
            elif opcao_c == 3:
                atualizar_conta(contas)
            elif opcao_c == 4:
                deletar_conta(contas)
            elif opcao_c == 5:
                pagar_conta(contas)
            elif opcao_c == 6:
                break
            else: 
                print("Opção inválida!")
                esperar()
                continue
            
                 