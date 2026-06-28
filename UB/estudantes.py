
from utils import limpar_tela, continuar, esperar
from persistencia import salvar_arquivo


def cadastrar_estudante(estudantes):
    limpar_tela()

    nome_e = input("Nome: ")
    data_nasc_e = input("Data de Nascimento: ")
    cpf_e = input("CPF: ")
    telefone_e = input("Número de Telefone: ")
    email_e = input("Email: ")

    while not cpf_e.isdigit() or len(cpf_e) != 11:
        cpf_e = input("CPF inválido. Digite novamente: ")

    while not telefone_e.isdigit() or len(telefone_e) != 9:
        telefone_e = input("Número de Telefone inválido. Digite novamente: ")
        
    if cpf_e in estudantes and estudantes[cpf_e][4]:
        print("CPF já cadastrado!")
        esperar()
    else:
        estudantes[cpf_e] = [
            nome_e, 
            data_nasc_e, 
            telefone_e, 
            email_e,
            True
            ]

        salvar_arquivo("estudantes.dat", estudantes)

        print("Estudante cadastrado com sucesso!")
        esperar()

def listar_estudantes(estudantes):
    limpar_tela()

    if not estudantes:
        print("Nenhum estudante cadastrado!")

    else:
        for cpf, dados in estudantes.items():

            if not dados[4]:
                continue    

            print("=" * 42)
            print(f"| {'DADOS DO ESTUDANTE':^38} |")
            print("=" * 42)

            print(f"| CPF: {cpf:<33} |")
            print(f"| Nome: {dados[0][:30]:<32} |")
            print(f"| Nascimento: {dados[1]:<26} |")
            print(f"| Telefone: {dados[2]:<28} |")
            print(f"| Email: {dados[3]:<31} |")
            print(f"| Status: {'ATIVO':<30} |")

            print("=" * 42)
        
        continuar()

def atualizar_estudante(estudantes):

    limpar_tela()   

    cpf_att_e = input("Informe o CPF do usuário: ")

    if cpf_att_e in estudantes and estudantes[cpf_att_e][4]:
        print("==" * 21)
        print("|        ATUALIZAÇÃO DE CADASTRO         |")
        print("==" * 21)
        print("|  1. NOME                               |")
        print("|  2. DATA DE NASCIMENTO                 |")
        print("|  3. CPF                                |")
        print("|  4. TELEFONE                           |")
        print("|  5. EMAIL                              |")
        print("|  6. ATUALIZAR TODOS OS DADOS           |")
        print("|  7. VOLTAR                             |")
        print("==" * 21)

        try:
            opcao_att = int(input("Qual informação deseja atualizar? "))
        except ValueError:
            print("Digite apenas números!")
            esperar()
            return

        if opcao_att == 1:
            limpar_tela()
            estudantes[cpf_att_e][0] = input("Novo nome: ")

        elif opcao_att == 2:
            limpar_tela()
            estudantes[cpf_att_e][1] = input("Nova data de nascimento: ")

        elif opcao_att == 4:
            limpar_tela()
            novo_telefone = input("Novo telefone: ")

            while not novo_telefone.isdigit() or len(novo_telefone) != 9:
                novo_telefone = input("Número de Telefone inválido. Digite novamente: ")

            estudantes[cpf_att_e][2] = novo_telefone

        elif opcao_att == 5:
            limpar_tela()
            estudantes[cpf_att_e][3] = input("Novo email: ")

        elif opcao_att == 3:
            limpar_tela()
            novo_cpf_e = input("Novo CPF: ")

            while not novo_cpf_e.isdigit() or len(novo_cpf_e) != 11:
                novo_cpf_e = input("CPF inválido. Digite novamente: ")

            if novo_cpf_e in estudantes and estudantes[novo_cpf_e][4] and novo_cpf_e != cpf_att_e:
                print("CPF já cadastrado!")
                esperar()
                return
            else:
                dados = estudantes.pop(cpf_att_e)
                estudantes[novo_cpf_e] = dados

        elif opcao_att == 6:
            limpar_tela()

            novo_nome_e = input("Nome: ")
            nova_data_e = input("Data de nascimento: ")
            novo_cpf_e = input("CPF: ")
            novo_telefone_e = input("Telefone: ")
            novo_email_e = input("Email: ")

            while not novo_cpf_e.isdigit() or len(novo_cpf_e) != 11:
                novo_cpf_e = input("CPF inválido. Digite novamente: ")

            while not novo_telefone_e.isdigit() or len(novo_telefone_e) != 9:
                novo_telefone_e = input("Número de Telefone inválido. Digite novamente: ")

            if novo_cpf_e in estudantes and estudantes[novo_cpf_e][4] and novo_cpf_e != cpf_att_e:
                print("CPF já cadastrado!")
                esperar()
                return

            dados = estudantes.pop(cpf_att_e)

            estudantes[novo_cpf_e] = [
                novo_nome_e,
                nova_data_e,
                novo_telefone_e,
                novo_email_e,
                dados[4]
            ]
                                
        elif opcao_att == 7:
            return
        
        else:
            print("Opção inválida!")
            esperar()
            return

        salvar_arquivo("estudantes.dat", estudantes)

        print("Cadastro atualizado com sucesso!")
        esperar()
        return

    else:
        print("CPF não encontrado!")
        esperar()
        return

def deletar_estudante(estudantes):
    limpar_tela()
    deletar_e = input("Informe o CPF do usuário: ")

    if deletar_e in estudantes and estudantes[deletar_e][4]:
        estudantes[deletar_e][4] = False

        salvar_arquivo("estudantes.dat", estudantes)

        print("Estudante removido com sucesso!")
        esperar()

    else:
        print("CPF não encontrado !")
        esperar()

def menu_estudantes(estudantes):
    while True:

        limpar_tela()

        print("==" * 21)
        print("|          MÓDULO DOS ESTUDANTES         |")
        print("==" * 21)
        print("|  1. CADASTRAR ESTUDANTES               |")
        print("|  2. LISTA DE ESTUDANTES                |")
        print("|  3. ATUALIZAR CADASTRO                 |")
        print("|  4. DELETAR ESTUDANTE                  |")
        print("|  5. VOLTAR                             |")
        print("==" * 21)
        print()

        try:
            opcao_e = int(input("Selecione uma das opções acima: "))
        except ValueError:
            print("Digite apenas números!")
            esperar()
            continue

        if opcao_e == 1:
            cadastrar_estudante(estudantes)
        elif opcao_e == 2:
            listar_estudantes(estudantes)
        elif opcao_e == 3:
            atualizar_estudante(estudantes)
        elif opcao_e == 4:
            deletar_estudante(estudantes)
        elif opcao_e == 5:
            break
        else:
            print("Opção inválida!")
            esperar()
            continue