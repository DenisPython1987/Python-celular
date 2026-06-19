from random import randint
from time import sleep

saudação = "\033[35mADVINHE O NÚMERO\033[m"
print("\033[35m-*-\033[m" * 20)
print(f"{saudação:^44}")
print("\033[35m-*-\033[m" * 20)

computador = randint(0, 50)

print("\033[35mEstou pensando em um número...")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1\033[m")
sleep(1)

while True:
    jogador = (input("\033[32mQual número você acha que eu pensei? \033[m"))
    if jogador.isdigit():
        jogada = int(jogador)
        if jogada < 0 or jogada > 50:
            print("\033[31mNúmero inválido. Digite um número entre 0 e 50.\033[m")
            continue
    else:
        print("\033[31mEntrada inválida! Digite um número entre 0 e 50.\033[m")
        continue
    if computador == jogada:
        print(f"\033[36mVOCÊ ACERTOU!!! Eu pensei no número {computador}.\033[m")
        break
    elif computador - jogada < 0:
        print(f"\033[32mVocê apostou muito alto. Eu pensei menos que {jogada}.\033[m")
        continue
    elif computador - jogada > 0:
        print(f"\033[32mVocê apostou baixo dessa vez. Eu pensei mais que {jogada}.\033[m")
        continue
