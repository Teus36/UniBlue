
from utils import limpar_tela, continuar, esperar
from persistencia import salvar_arquivo, proximo_id


def cadastrar_gasto(gastos, estudantes):
    limpar_tela()

    descricao_g = input("Descrição: ")
    valor_g = float(input("Valor: "))
    responsavel_g = input("CPF do responsável: ")
    data_g = input("Data: ")
    

    if responsavel_g not in estudantes or not estudantes[responsavel_g][4]:
        print("Responsável inválido!")
        esperar()
        return

    id_gasto = proximo_id(gastos)

    gastos[id_gasto] = [
        descricao_g,
        valor_g,
        responsavel_g,
        data_g,
        True
    ]

    salvar_arquivo("gastos.dat", gastos)

    print(f"Gasto cadastrado com ID {id_gasto}!")

    esperar()

def listar_gastos(gastos):
    limpar_tela()

    if not gastos:
        print("Nenhum gasto cadastrado!")

    else:
        for id_g, dados in gastos.items():

            if not dados[4]:
                continue

            print("=" * 42)
            print(f"| {'DADOS DO GASTO':^38} |")
            print("=" * 42)

            print(f"| ID: {id_g:<34} |")
            print(f"| Descrição: {dados[0][:25]:<27} |")
            print(f"| Valor: R$ {dados[1]:<28} |")
            print(f"| Responsável: {dados[2]:<25} |")
            print(f"| Data: {dados[3]:<32} |")
            print(f"| Status: {'ATIVO':<30} |")

            print("=" * 42)

    continuar()

def atualizar_gasto(gastos, estudantes):
    limpar_tela()

    id_att_g = str(input("Informe o ID do gasto: "))

    if id_att_g in gastos and gastos[id_att_g][4]:

        print("==" * 21)
        print("|          ATUALIZAÇÃO DE GASTO          |")
        print("==" * 21)
        print("|  1. DESCRIÇÃO                          |")
        print("|  2. VALOR                              |")
        print("|  3. RESPONSÁVEL                        |")
        print("|  4. DATA                               |")
        print("|  5. ATUALIZAR TODOS OS DADOS           |")
        print("|  6. VOLTAR                             |")
        print("==" * 21)

        try:
            opcao_att_g = int(input("Qual informação deseja atualizar? "))
        except ValueError:
            print("Digite apenas números!")
            esperar()
            return

        if opcao_att_g == 1:
            gastos[id_att_g][0] = input("Nova descrição: ")

        elif opcao_att_g == 2:
            gastos[id_att_g][1] = float(input("Novo valor: "))

        elif opcao_att_g == 3:
            novo_resp = input("Novo responsável: ")

            if novo_resp not in estudantes or not estudantes[novo_resp][4]:
                print("Responsável inválido!")
                esperar()
            else:
                gastos[id_att_g][2] = novo_resp

        elif opcao_att_g == 4:
            gastos[id_att_g][3] = input("Nova data: ")

        elif opcao_att_g == 5:

            nova_descricao_g = input("Descrição: ")
            novo_valor_g = float(input("Valor: "))
            novo_responsavel_g = input("Responsável: ")
            nova_data_g = input("Data: ")

            if novo_responsavel_g not in estudantes or not estudantes[novo_responsavel_g][4]:
                print("Responsável inválido!")
                esperar()
                return
            
            status_g = gastos[id_att_g][4]

            gastos[id_att_g] = [
                nova_descricao_g,
                novo_valor_g,
                novo_responsavel_g,
                nova_data_g,
                status_g
            ]

        elif opcao_att_g == 6:
            return   
        
        else:
            print("Opção inválida!")
            esperar()
            return

        salvar_arquivo("gastos.dat", gastos)

        print("Gasto atualizado com sucesso!")
        esperar()
        return

    else:
        print("ID não encontrado!")

    esperar()

def deletar_gasto(gastos):
    limpar_tela()

    deletar_g = str(input("Informe o ID do gasto: "))

    if deletar_g in gastos and gastos[deletar_g][4]:
        gastos[deletar_g][4] = False

        salvar_arquivo("gastos.dat", gastos)

        print("Gasto removido com sucesso!")

    else:
        print("ID não encontrado!")

    esperar()

def menu_gastos(gastos,estudantes):
    while True:
            limpar_tela()
            print("==" * 21)
            print("|            MÓDULO DOS GASTOS           |")
            print("==" * 21)
            print("|  1. CADASTRAR GASTO                    |")
            print("|  2. LISTAR GASTOS                      |")
            print("|  3. ATUALIZAR GASTO                    |")
            print("|  4. DELETAR GASTO                      |")
            print("|  5. VOLTAR                             |")
            print("==" * 21)
            print()
            
            try:
                opcao_g = int(input("Selecione uma das opções acima: "))
            except ValueError:
                print("Digite apenas números!")
                esperar()
                continue

            if opcao_g == 1:
                cadastrar_gasto(gastos, estudantes)
            elif opcao_g == 2:
                listar_gastos(gastos)
            elif opcao_g == 3:
                atualizar_gasto(gastos, estudantes)
            elif opcao_g == 4:
                deletar_gasto(gastos)
            elif opcao_g == 5:
                break
            else:
                print("Opção inválida")
                esperar()
                continue