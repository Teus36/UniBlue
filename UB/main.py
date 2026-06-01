print("==" * 21)
print("|  SISTEMA DE GESTÃO DESPESAS UNIBLUE  |")
print("==" * 21)
print("|  1. ESTUDANTES                         |")
print("|  2. GASTOS                             |")
print("|  3. CONTAS                             |")
print("|  4. RELATÓRIOS                         |")
print("|  5. SOBRE O SISTEMA                    |")
print("|  6. SAIR                               |")
print("==" * 21)

estudantes = {}

while True:
    opcao = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))
    voltar = False

    while True: 
        if opcao == 1:
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
            print()

            opcao_e = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))

            if opcao_e == 1:
                nome_e = str(input("Nome: "))
                data_nasc_e = str(input("Data de Nascimento: "))
                cpf_e = str(input("CPF: "))
                telefone_e = str(input("Número de Telefone: "))
                email_e = str(input("Email: "))

                while len(cpf_e) !=11:
                    cpf_e = str(input("CPF: "))
                    
                estudantes = {cpf_e: [nome_e, data_nasc_e, telefone_e, email_e]}
                print(f"Estudante cadastrado: {estudantes}")

            if opcao_e == 2:
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
                    
            if opcao_e == 3: 
                atualizar_cadastro_e = str(input("Informe o CPF do usuário: "))
                voltar = False
                largura = 60

                while True:
                    for chave, valor in estudantes.items():
                        if atualizar_cadastro_e == chave:
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
                            print()

                            opcao_att = int(input("Qual informação deseja atualizar? "))

                            if opcao_att == 1:
                                nome_e = str(input("Nome: "))
                                estudantes[chave][0] = nome_e
                            elif opcao_att == 2:
                                data_nasc_e = str(input("Data de Nascimento: "))
                                estudantes[chave][1] = data_nasc_e
                            elif opcao_att == 3:
                                cpf_e = str(input("CPF: "))
                                estudantes[chave][2] = cpf_e
                            elif opcao_att == 4:
                                telefone_e = str(input("Número de Telefone: "))
                                estudantes[chave][3] = telefone_e
                            elif opcao_att == 5:
                                email_e = str(input("Email: "))
                                estudantes[chave][4] = email_e
                            elif opcao_att == 6:
                                nome_e = str(input("Nome: "))
                                data_nasc_e = str(input("Data de Nascimento: "))
                                cpf_e = str(input("CPF: "))
                                telefone_e = str(input("Número de Telefone: "))
                                email_e = str(input("Email: "))

                                estudantes = {cpf_e: [nome_e, data_nasc_e, telefone_e, email_e]}
                            elif opcao_att == 7:
                                voltar = True
                                break
                        
                        else:
                            print("CPF NÃO ENCONTRADO!!!")

                    if voltar == True:
                        break
                    
            
            elif opcao_e == 4:
                deletar_e = input("Informe o CPF do usuário: ")

                if deletar_e in estudantes:
                    del estudantes[deletar_e]
                    print("Estudante removido com sucesso!")
                else:
                    print("CPF não encontrado.")
                

        elif opcao == 5:
            if voltar == True:
                break


    if opcao == 2:
        print("==" * 21)
        print("|            MÓDULO DOS GASTOS           |")
        print("==" * 21)
        print("|           EM DESENVOLVIMENTO           |")
        print("==" * 21)
        print()

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

    else:
        break
