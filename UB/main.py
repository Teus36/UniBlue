import os
import time
import pickle 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

estudantes = {'71403700443':["Mateus Batista Almeida","13/11/2006","999778632","mtb@gmail.com"]}
gastos = {'1':["Pizza G", "45","71403700443","10/06/2026"]}
contas = {'1':["Conta de Luz","180","30/06/2026","PENDENTE"]}
id_gasto = 2 
id_conta = 2

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
                    estudantes[cpf_e] = [
                        nome_e, 
                        data_nasc_e, 
                        telefone_e, 
                        email_e]
                    
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
                    print("|  7. VOLTAR                             |")
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

                elif opcao_att == 7:
                    break

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

            opcao_g = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))

            if opcao_g == 1:
                limpar_tela()

                descricao_g = input("Descrição: ")
                valor_g = float(input("Valor: "))
                responsavel_g = input("CPF do responsável: ")
                data_g = input("Data: ")

                gastos[id_gasto] = [
                    descricao_g,
                    valor_g,
                    responsavel_g,
                    data_g
                ]

                print(f"Gasto cadastrado com ID {id_gasto}!")

                id_gasto += 1

                time.sleep(2)

            elif opcao_g == 2:
                limpar_tela()

                if not gastos:
                    print("Nenhum gasto cadastrado!")

                else:
                    for id_g, dados in gastos.items():

                        print("=" * 42)
                        print(f"| {'DADOS DO GASTO':^38} |")
                        print("=" * 42)

                        print(f"| ID: {str(id_g):<34} |")
                        print(f"| Descrição: {dados[0][:25]:<27} |")
                        print(f"| Valor: R$ {str(dados[1]):<28} |")
                        print(f"| Responsável: {dados[2]:<25} |")
                        print(f"| Data: {dados[3]:<32} |")

                        print("=" * 42)

                input("Pressione ENTER para continuar...")

            elif opcao_g == 3:
                limpar_tela()

                id_att_g = int(input("Informe o ID do gasto: "))

                if id_att_g in gastos:

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

                    opcao_att_g = int(input("O que deseja atualizar? "))

                    if opcao_att_g == 1:
                        gastos[id_att_g][0] = input("Nova descrição: ")

                    elif opcao_att_g == 2:
                        gastos[id_att_g][1] = float(input("Novo valor: "))

                    elif opcao_att_g == 3:
                        gastos[id_att_g][2] = input("Novo responsável: ")

                    elif opcao_att_g == 4:
                        gastos[id_att_g][3] = input("Nova data: ")

                    elif opcao_att_g == 5:

                        descricao_g = input("Descrição: ")
                        valor_g = float(input("Valor: "))
                        responsavel_g = input("Responsável: ")
                        data_g = input("Data: ")

                        gastos[id_att_g] = [
                            descricao_g,
                            valor_g,
                            responsavel_g,
                            data_g
                        ]

                    elif opcao_att_g == 6:
                        continue

                    print("Gasto atualizado com sucesso!")

                else:
                    print("ID não encontrado!")

                time.sleep(2)

            elif opcao_g == 4:
                limpar_tela()

                deletar_g = int(input("Informe o ID do gasto: "))

                if deletar_g in gastos:
                    del gastos[deletar_g]
                    print("Gasto removido com sucesso!")

                else:
                    print("ID não encontrado!")

                time.sleep(2)

            elif opcao_g == 5:
                break


    elif opcao == 3:
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

            opcao_c = int(input("SELECIONE UMA DAS OPÇÕES ACIMA: "))

            if opcao_c == 1:
                limpar_tela()

                nome_c = input("Nome da conta: ")
                valor_c = float(input("Valor da conta: "))
                vencimento_c = input("Data de vencimento: ")

                contas[id_conta] = [
                    nome_c,
                    valor_c,
                    vencimento_c,
                    "PENDENTE"
                ]

                print(f"Conta cadastrada com ID {id_conta}!")

                id_conta += 1

                time.sleep(2)

            elif opcao_c == 2:
                limpar_tela()

                if not contas:
                    print("Nenhuma conta cadastrada!")

                else:
                    for id_c, dados in contas.items():

                        print("=" * 42)
                        print(f"| {'DADOS DA CONTA':^38} |")
                        print("=" * 42)

                        print(f"| ID: {str(id_c):<34} |")
                        print(f"| Conta: {dados[0][:28]:<30} |")
                        print(f"| Valor: R$ {str(dados[1]):<25} |")
                        print(f"| Vencimento: {dados[2]:<24} |")
                        print(f"| Status: {dados[3]:<29} |")

                        print("=" * 42)

                input("Pressione ENTER para continuar...")

            elif opcao_c == 3:
                limpar_tela()

                id_att_c = int(input("Informe o ID da conta: "))

                if id_att_c in contas:

                    print("==" * 21)
                    print("|         ATUALIZAÇÃO DE CONTA           |")
                    print("==" * 21)
                    print("|  1. NOME DA CONTA                      |")
                    print("|  2. VALOR                              |")
                    print("|  3. VENCIMENTO                         |")
                    print("|  4. STATUS                             |")
                    print("|  5. ATUALIZAR TODOS OS DADOS           |")
                    print("|  6. VOLTAR                             |")
                    print("==" * 21)

                    opcao_att_c = int(input("O que deseja atualizar? "))

                    if opcao_att_c == 1:
                        contas[id_att_c][0] = input("Novo nome da conta: ")

                    elif opcao_att_c == 2:
                        contas[id_att_c][1] = float(input("Novo valor: "))

                    elif opcao_att_c == 3:
                        contas[id_att_c][2] = input("Novo vencimento: ")

                    elif opcao_att_c == 4:
                        contas[id_att_c][3] = input("Novo status: ")

                    elif opcao_att_c == 5:

                        nome_c = input("Nome da conta: ")
                        valor_c = float(input("Valor: "))
                        vencimento_c = input("Vencimento: ")
                        status_c = input("Status: ")

                        contas[id_att_c] = [
                            nome_c,
                            valor_c,
                            vencimento_c,
                            status_c
                        ]

                    elif opcao_att_c == 6:
                        continue

                    print("Conta atualizada com sucesso!")

                else:
                    print("ID não encontrado!")

                time.sleep(2)

            elif opcao_c == 4:
                limpar_tela()

                deletar_c = int(input("Informe o ID da conta: "))

                if deletar_c in contas:
                    del contas[deletar_c]
                    print("Conta removida com sucesso!")
                else:
                    print("ID não encontrado!")

                time.sleep(2)


            elif opcao_c == 5:
                limpar_tela()

                id_pagar_c = int(input("Informe o ID da conta: "))

                if id_pagar_c in contas:
                    contas[id_pagar_c][3] = "PAGA"
                    print("Conta marcada como paga!")
                else:
                    print("ID não encontrado!")

                time.sleep(2)

            elif opcao_c == 6:
                break
    
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