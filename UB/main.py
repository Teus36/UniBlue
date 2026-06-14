import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

estudantes = {}
gastos = {}

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

    opcao = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))

    if opcao == 1:
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

            opcao_e = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))

            if opcao_e == 1:
                limpar_tela()   

                nome_e = str(input("Nome: "))
                data_nasc_e = str(input("Data de Nascimento: "))
                cpf_e = str(input("CPF: "))
                telefone_e = str(input("Número de Telefone: "))
                email_e = str(input("Email: "))

                while not cpf_e.isdigit() or len(cpf_e) != 11:
                    cpf_e = input("CPF inválido. Digite novamente: ")

                while not telefone_e.isdigit() or len(telefone_e) != 9:
                    telefone_e = str(input("Número de Telefone inválido. Digite novamente: "))   
                    
                if cpf_e in estudantes:
                    print("CPF já cadastrado!")
                    time.sleep(2)
                else:
                    estudantes[cpf_e] = [nome_e, data_nasc_e, telefone_e, email_e]
                    print("Estudante cadastrado com sucesso!")
                    time.sleep(2)

            elif opcao_e == 2:
                limpar_tela()

                if not estudantes:
                    print("Nenhum estudante cadastrado!")

                else:
                    for cpf, dados in estudantes.items():
                        print("=" * 42)
                        print(f"| {'DADOS DO ESTUDANTE':^38} |")
                        print("=" * 42)

                        print(f"| CPF: {cpf:<33} |")
                        print(f"| Nome: {dados[0][:30]:<32} |")
                        print(f"| Nascimento: {dados[1]:<26} |")
                        print(f"| Telefone: {dados[2]:<28} |")
                        print(f"| Email: {dados[3]:<31} |")

                        print("=" * 42)
                    
                    seguir = input("Pressione ENTER para continuar...")
                    
            elif opcao_e == 3: 
                limpar_tela()   

                cpf_att_e = str(input("Informe o CPF do usuário: "))

                if cpf_att_e in estudantes:
                    print("==" * 21)
                    print("|        ATUALIZAÇÃO DE CADASTRO         |")
                    print("==" * 21)
                    print("|  1. NOME                               |")
                    print("|  2. DATA DE NASCIMENTO                 |")
                    print("|  3. CPF                                |")
                    print("|  4. TELEFONE                           |")
                    print("|  5. EMAIL                              |")
                    print("|  6. ATUALIZAR TODOS OS DADOS           |")
                    print("==" * 21)

                    opcao_att = int(input("Qual informação deseja atualizar? "))

                    if opcao_att == 1:
                        limpar_tela()
                        estudantes[cpf_att_e][0] = input("Novo nome: ")

                    elif opcao_att == 2:
                        limpar_tela()
                        estudantes[cpf_att_e][1] = input("Nova data de nascimento: ")

                    elif opcao_att == 4:
                        limpar_tela()
                        estudantes[cpf_att_e][2] = input("Novo telefone: ")

                        while not telefone_e.isdigit() or len(telefone_e) != 9:
                            telefone_e = str(input("Número de Telefone inválido. Digite novamente: "))   

                    elif opcao_att == 5:
                        limpar_tela()
                        estudantes[cpf_att_e][3] = input("Novo email: ")

                    elif opcao_att == 3:
                        limpar_tela()
                        novo_cpf = input("Novo CPF: ")

                        while not novo_cpf.isdigit() or len(novo_cpf) != 11:
                            novo_cpf = input("CPF inválido. Digite novamente: ")
                            
                        if novo_cpf in estudantes and novo_cpf != cpf_att_e:
                            print("CPF já cadastrado!")
                            time.sleep(2)
                        else:
                            del estudantes[cpf_att_e]
                            estudantes[novo_cpf] = [nome, data, telefone, email]

                    elif opcao_att == 6:
                        limpar_tela()

                        nome = input("Nome: ")
                        data = input("Data de nascimento: ")
                        novo_cpf = input("CPF: ")
                        telefone = input("Telefone: ")
                        email = input("Email: ")

                        del estudantes[cpf_att_e]
                        estudantes[novo_cpf] = [nome, data, telefone, email]

                    print("Cadastro atualizado com sucesso!")
                    time.sleep(2)

                else:
                    print("CPF não encontrado!")
                                
            
            elif opcao_e == 4:
                limpar_tela()
                deletar_e = input("Informe o CPF do usuário: ")

                if deletar_e in estudantes:
                    del estudantes[deletar_e]
                    print("Estudante removido com sucesso!")
                else:
                    print("CPF não encontrado !")
                

            elif opcao_e == 5:
                break


    if opcao == 2:
        while True:
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

            opcao_g = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))


    elif opcao == 3:
        print("==" * 21)
        print("|            MURAL DE AVISOS             |")
        print("==" * 21)
        print("|           EM DESENVOLVIMENTO           |")
        print("==" * 21)
        print()
    
    elif opcao == 4:
        print("==" * 21)
        print("|               RELATÓRIOS               |")
        print("==" * 21)
        print("|           EM DESENVOLVIMENTO           |")
        print("==" * 21)
        print()

    elif opcao == 5:
        print("==" * 21)
        print("|            SOBRE O SISTEMA             |")
        print("==" * 21)
        print("|           EM DESENVOLVIMENTO           |")
        print("==" * 21)
        print()

    elif opcao == 6:
        break