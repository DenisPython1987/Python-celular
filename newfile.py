import random

enforcado = ["----------------------- \n",
    "                | \n", "                0 \n ", "                 | \n ",
    "               /  ", "\\ \n", "                 | \n", "               /  ","\\"]

#print(linha, '\n', corda, '\n', cabeca, '\n', pescoco, '\n', braco_esq + braco_dir, '\n', corpo, '\n', perna_esq + perna_dir)

palavras = ['abacaxi', 'alface', 'palavra', 'automóvel', 'pelúcia', 'amante']

palavra = random.choice(palavras)

incognita = ['_' * len(palavra)]

jogo = True

print(incognita)

cont_perder = 0
cont_vitoria = 0

while jogo == True:
    chute = str(input('Tente uma letra: '))
    for i, j in enumerate(palavra):
        if chute == i:
            incognita[j] = chute
            cont_vitoria += 1
            print(incognita)
        else:
            cont_perder += 1
            print(enforcado[:cont_perder - 1])
            print("Você errou! Tente novamente.")
            if cont_perder == len(palavra):
                print(f"Você perdeu! A palavra era {palavra}")
                jogo = False
                break
            
