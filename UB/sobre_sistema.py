import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def sobre_sistema():
    limpar_tela()

    print("=" * 70)
    print(" " * 28 + "UNIBLUE")
    print("=" * 70)

    print("\nO UniBlue é um sistema de gestão financeira desenvolvido")
    print("para auxiliar repúblicas estudantis no controle de")
    print("despesas, contas e informações dos moradores.")
    print("\nSeu principal objetivo é facilitar a organização")
    print("financeira compartilhada, promovendo transparência,")
    print("controle e uma melhor divisão dos gastos.")

    print("\n" + "=" * 70)
    print("FUNCIONALIDADES")
    print("=" * 70)

    print("\n[1] Módulo de Estudantes")
    print("- Cadastro de estudantes")
    print("- Listagem de estudantes")
    print("- Atualização de informações")
    print("- Exclusão de estudantes")

    print("\n[2] Módulo de Gastos")
    print("- Registro de despesas")
    print("- Consulta de gastos")
    print("- Atualização de registros")
    print("- Exclusão de gastos")
    print("- Histórico de despesas")

    print("\n[3] Módulo de Contas")
    print("- Cadastro de contas fixas")
    print("- Controle de vencimentos")
    print("- Atualização de informações")
    print("- Exclusão de contas")
    print("- Acompanhamento de contas")

    print("\n[4] Módulo de Relatórios")
    print("- Relatório de estudantes")
    print("- Relatório de gastos")
    print("- Relatório de contas")
    print("- Resumo financeiro")

    print("\n[5] Sobre o Sistema")
    print("- Objetivo do sistema")
    print("- Informações do projeto")
    print("- Descrição dos módulos")
    print("- Versão do sistema")
    print("- Créditos dos desenvolvedores")
    print("- Informações de uso")

    print("\n" + "=" * 70)
    print("TECNOLOGIAS UTILIZADAS")
    print("=" * 70)

    print("- Python")
    print("- Estruturas de Dados (Listas e Dicionários)")
    print("- Programação Estruturada")

    print("\n" + "=" * 70)
    print("PÚBLICO-ALVO")
    print("=" * 70)

    print("- Repúblicas estudantis")
    print("- Moradias compartilhadas")
    print("- Grupos de estudantes")

    print("\n" + "=" * 70)
    print("SOBRE O NOME")
    print("=" * 70)

    print("Uni   -> Universidade / Universitários")
    print("Blue  -> Referência à expressão 'estar no azul',")
    print("         representando estabilidade financeira.")

    print("\nO nome representa o objetivo do sistema:")
    print("ajudar estudantes a manterem suas finanças")
    print("organizadas e sempre no azul.")

    print("\n" + "=" * 70)
    print("VERSÃO")
    print("=" * 70)
    print("UniBlue v1.0")

    print("\nProjeto desenvolvido para fins acadêmicos e educacionais.")

    input("\nPressione ENTER para voltar ao menu...")