import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    input("Pressione ENTER para continuar...")

def esperar():
    time.sleep(2)
    