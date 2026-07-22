from Utilidades.apresentação import cabeçalho, adaptado
from Utilidades.números import leia_int
from Utilidades.escolha_continuar import continuar
from Utilidades.cores import cor_aleatória, cor_final
opções = ('pedra', 'papel', 'tesoura')
def jogada():
    cor_aleatória()
    print("""
    Escolha uma opcão:
    
    1 - Papel
    2 - Pedra
    3 - Tesoura""")
    cor_final()
    while True:
        cor_aleatória()
        escolha = leia_int("Sua escolha: ")
        cor_final()
        if escolha < 1 or escolha > 3:
            cor_aleatória()
            print("Opção inválida. Escolha uma opção entre 1 e 3!")
            cor_final()
            continue
        if 0 < escolha < 4:
            final = opções[escolha - 1]
        return final

def jogada_computador():
    from random import randint
    parcial = randint(0, 2)
    final = opções[parcial]
    return final
    
def vitória(comp, jog):
    if (comp == 'papel' and jog == 'pedra') or (comp == 'pedra' and jog == 'tesoura') or (comp == 'tesoura' and jog == 'papel'):
        cor_aleatória()
        adaptado("COMPUTADOR GANHOU")
        cor_final()
    if (jog == 'papel' and comp == 'pedra') or (jog == 'pedra' and comp == 'tesoura') or (jog == 'tesoura' and comp == 'papel'):
        cor_aleatória()
        adaptado("JOGADOR GANHOU")
        cor_final()
    if (jog == 'papel' and comp == 'papel') or (jog == 'pedra' and comp == 'pedra') or (jog == 'tesoura' and comp == 'tesoura'):
        cor_aleatória()
        adaptado("EMPATE")
        cor_final()

while True:
    cabeçalho("JOKENPO")
    jogador = jogada()
    computador = jogada_computador()
    vitória(computador, jogador)
    escolha = continuar()
    if escolha == "N":
        break
        
cabeçalho("Obrigado po jogar")
    
    