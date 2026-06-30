from utils import limpar_tela, continuar, esperar


def relatorio_estudantes(estudantes):
    limpar_tela()

    if not estudantes:
        print("Nenhum estudante cadastrado!")
        continuar()
        return

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


def buscar_estudante(estudantes):
    limpar_tela()

    cpf = input("Informe o CPF: ")

    if cpf not in estudantes or not estudantes[cpf][4]:
        print("Estudante não encontrado!")
        esperar()
        return

    dados = estudantes[cpf]

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


def listar_gastos_relatorio(gastos):
    limpar_tela()

    if not gastos:
        print("Nenhum gasto cadastrado!")
        continuar()
        return

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


def buscar_gasto(gastos):
    limpar_tela()

    id_g = input("Informe o ID do gasto: ")

    if id_g not in gastos or not gastos[id_g][4]:
        print("Gasto não encontrado!")
        esperar()
        return

    dados = gastos[id_g]

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


def gastos_por_estudante(estudantes, gastos):
    limpar_tela()

    cpf = input("Informe o CPF do estudante: ")

    if cpf not in estudantes or not estudantes[cpf][4]:
        print("Estudante não encontrado!")
        esperar()
        return

    print("=" * 42)
    print(f"Estudante: {estudantes[cpf][0]}")
    print(f"CPF: {cpf}")
    print("=" * 42)

    encontrou = False
    total = 0

    for id_g, dados in gastos.items():

        if not dados[4]:
            continue

        if dados[2] == cpf:

            encontrou = True
            total += dados[1]

            print(f"ID: {id_g}")
            print(f"Descrição: {dados[0]}")
            print(f"Valor: R$ {dados[1]:.2f}")
            print(f"Data: {dados[3]}")
            print("-" * 42)

    if not encontrou:
        print("Esse estudante não possui gastos cadastrados.")
    else:
        print(f"TOTAL GASTO: R$ {total:.2f}")

    continuar()

def listar_contas_relatorio(contas):
    limpar_tela()

    if not contas:
        print("Nenhuma conta cadastrada!")
        continuar()
        return

    for id_c, dados in contas.items():

        if not dados[4]:
            continue

        print("=" * 42)
        print(f"| {'DADOS DA CONTA':^38} |")
        print("=" * 42)

        print(f"| ID: {id_c:<34} |")
        print(f"| Conta: {dados[0][:28]:<31} |")
        print(f"| Valor: R$ {dados[1]:<28} |")
        print(f"| Vencimento: {dados[2]:<26} |")
        print(f"| Situação: {dados[3]:<28} |")
        print(f"| Status: {'ATIVO':<30} |")

        print("=" * 42)

    continuar()


def contas_pendentes(contas):
    limpar_tela()

    encontrou = False

    for id_c, dados in contas.items():

        if not dados[4]:
            continue

        if dados[3] == "PENDENTE":

            encontrou = True

            print("=" * 42)
            print(f"| {'CONTA PENDENTE':^38} |")
            print("=" * 42)

            print(f"| ID: {id_c:<34} |")
            print(f"| Conta: {dados[0][:28]:<31} |")
            print(f"| Valor: R$ {dados[1]:<28} |")
            print(f"| Vencimento: {dados[2]:<26} |")

            print("=" * 42)

    if not encontrou:
        print("Nenhuma conta pendente.")

    continuar()


def contas_pagas(contas):
    limpar_tela()

    encontrou = False

    for id_c, dados in contas.items():

        if not dados[4]:
            continue

        if dados[3] == "PAGA":

            encontrou = True

            print("=" * 42)
            print(f"| {'CONTA PAGA':^38} |")
            print("=" * 42)

            print(f"| ID: {id_c:<34} |")
            print(f"| Conta: {dados[0][:28]:<31} |")
            print(f"| Valor: R$ {dados[1]:<28} |")
            print(f"| Vencimento: {dados[2]:<26} |")

            print("=" * 42)

    if not encontrou:
        print("Nenhuma conta paga.")

    continuar()


def total_gastos(gastos):
    limpar_tela()

    total = 0

    for dados in gastos.values():

        if not dados[4]:
            continue

        total += dados[1]

    print(f"TOTAL DE GASTOS: R$ {total:.2f}")

    continuar()


def total_contas_pendentes(contas):
    limpar_tela()

    total = 0

    for dados in contas.values():

        if not dados[4]:
            continue

        if dados[3] == "PENDENTE":
            total += dados[1]

    print(f"TOTAL DE CONTAS PENDENTES: R$ {total:.2f}")

    continuar()


def total_por_estudante(estudantes, gastos):
    limpar_tela()

    if not estudantes:
        print("Nenhum estudante cadastrado!")
        continuar()
        return

    for cpf, estudante in estudantes.items():

        if not estudante[4]:
            continue

        total = 0

        for gasto in gastos.values():

            if not gasto[4]:
                continue

            if gasto[2] == cpf:
                total += gasto[1]

        print("=" * 42)
        print(f"Nome: {estudante[0]}")
        print(f"CPF: {cpf}")
        print(f"Total gasto: R$ {total:.2f}")
        print("=" * 42)

    continuar()


def resumo_geral(estudantes, gastos, contas):
    limpar_tela()

    estudantes_ativos = 0
    gastos_ativos = 0
    contas_ativas = 0
    contas_pagas = 0
    contas_pendentes = 0

    total_gastos = 0
    total_pendente = 0

    for dados in estudantes.values():

        if dados[4]:
            estudantes_ativos += 1

    for dados in gastos.values():

        if dados[4]:
            gastos_ativos += 1
            total_gastos += dados[1]

    for dados in contas.values():

        if not dados[4]:
            continue

        contas_ativas += 1

        if dados[3] == "PAGA":
            contas_pagas += 1
        else:
            contas_pendentes += 1
            total_pendente += dados[1]

    print("=" * 42)
    print(f"| {'RESUMO GERAL':^38} |")
    print("=" * 42)

    print(f"| Estudantes ativos: {estudantes_ativos:<18}|")
    print(f"| Gastos ativos: {gastos_ativos:<22}|")
    print(f"| Contas ativas: {contas_ativas:<22}|")
    print(f"| Contas pagas: {contas_pagas:<23}|")
    print(f"| Contas pendentes: {contas_pendentes:<18}|")
    print(f"| Total de gastos: R$ {total_gastos:<15.2f}|")
    print(f"| Total pendente: R$ {total_pendente:<16.2f}|")

    print("=" * 42)

    continuar()


def menu_relatorios(estudantes, gastos, contas):

    while True:

        limpar_tela()

        print("==" * 21)
        print("|             RELATÓRIOS                 |")
        print("==" * 21)
        print("| 1. LISTAR ESTUDANTES                   |")
        print("| 2. BUSCAR ESTUDANTE POR CPF            |")
        print("| 3. LIGASTAR GASTOS                     |")
        print("| 4. BUSCAR GASTO POR ID                 |")
        print("| 5. GASTOS POR ESTUDANTE                |")
        print("| 6. LISTAR CONTAS                       |")
        print("| 7. CONTAS PENDENTES                    |")
        print("| 8. CONTAS PAGAS                        |")
        print("| 9. TOTAL DE GASTOS                     |")
        print("|10. TOTAL DE CONTAS PENDENTES           |")
        print("|11. TOTAL GASTO POR ESTUDANTE           |")
        print("|12. RESUMO GERAL                        |")
        print("|13. VOLTAR                              |")
        print("==" * 21)

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            esperar()
            continue

        if opcao == 1:
            relatorio_estudantes(estudantes)

        elif opcao == 2:
            buscar_estudante(estudantes)

        elif opcao == 3:
            listar_gastos_relatorio(gastos)

        elif opcao == 4:
            buscar_gasto(gastos)

        elif opcao == 5:
            gastos_por_estudante(estudantes, gastos)

        elif opcao == 6:
            listar_contas_relatorio(contas)

        elif opcao == 7:
            contas_pendentes(contas)

        elif opcao == 8:
            contas_pagas(contas)

        elif opcao == 9:
            total_gastos(gastos)

        elif opcao == 10:
            total_contas_pendentes(contas)

        elif opcao == 11:
            total_por_estudante(estudantes, gastos)

        elif opcao == 12:
            resumo_geral(estudantes, gastos, contas)

        elif opcao == 13:
            break

        else:
            print("Opção inválida!")
            esperar()