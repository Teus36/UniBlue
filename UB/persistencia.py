import pickle

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "rb") as arq:
            return pickle.load(arq)

    except (FileNotFoundError, EOFError):
        with open(nome_arquivo, "wb") as arq:
            pickle.dump({}, arq)

        return {}

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "wb") as arq:
        pickle.dump(dados, arq)

def proximo_id(dicionario):
    if not dicionario:
        return "1"

    return str(max(map(int, dicionario.keys())) + 1)