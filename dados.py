from random import randint
from time import sleep
from Utilidades.escolha_continuar import continuar

def carregando():
    print("\033[35mAguarde, carregando", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".\033[m")
    
def linha():
    print("\033[35m-=-\033[m" * 20)

while True:
    linha()
    carregando()
    dado_1 = randint(1, 6)
    print(f"\033[33mO jogador 1 jogou: {dado_1}\033[m")
    linha()
    carregando()
    dado_2 = randint(1, 6)
    print(f"\033[31mO jogador 2 jogou: {dado_2}\033[m")
    linha()
    if dado_1 > dado_2:
        print("\033[36mJogador 1 ganhou\033[m")
    elif dado_1 < dado_2:
        print("\033[36mJogador 2 ganhou\033[m")
    else:
        print("\033[36mEmpate!\033[m")
    linha()
    
    escolha = continuar()
    if escolha == "N":
        break