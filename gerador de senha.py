from random import choice, randint

#Apresentação
apresentação = "\033[35mGeredor de senhas\033[m"
print("\033[35m-*-\033[m" * 20)
print(f"{apresentação:^40}")
print("\033[35m-*-\033[m" * 20)


alfabeto_minúsculo = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
alfabeto_maiúsculo = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
números = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
símbolos = ('(', ')', '[', ']', ';', '?', '!', '-', '_', '*', '+', '%')

lista_parcial = []
senha_parcial = []
tamanho_randint = 0

lista_parcial.append(números)

while True:
    tamanho = int(input("Digite o tamanho da senha: "))
    carac_esp = int(input("Você quer caracteres especiais na sua senha? Digite 1 para sim ou 2 para não: "))
    if carac_esp < 1 or carac_esp > 2:
        print('Opção inválida, tente novamente!')
        continue
    elif carac_esp == 1:
        lista_parcial.append(símbolos)
    letras_maiu = int(input("Você quer letras maiúsculas na sua senha? Digite 1 para sim ou 2 para não: "))
    if letras_maiu < 1 or letras_maiu > 2:
        print("Opção inválida, tente novamente!")
        continue
    elif letras_maiu == 1:
        lista_parcial.append(alfabeto_maiúsculo)
    letras_minu = int(input("Você quer letras minúsculas na sua senha? Digite 1 para sim ou 2 para não: "))
    if letras_minu < 1 or letras_minu > 2:
        print("Opção inválida, tente novamente!")
        continue
    elif letras_minu == 1:
        lista_parcial.append(alfabeto_minúsculo)
    break
        
for i in range(0, tamanho + 1):
    if len(lista_parcial) == 1:
        senha_parcial.append(choice(lista_parcial[0]))
    elif len(lista_parcial) == 2:
        escolha = randint(0, 1)
        senha_parcial.append(choice(lista_parcial[escolha]))
    elif len(lista_parcial) == 3:
        escolha = randint(0, 2)
        senha_parcial.append(choice(lista_parcial[escolha]))
    elif len(lista_parcial) == 4:
        escolha = randint(0, 3)
        senha_parcial.append(choice(lista_parcial[escolha]))
        
senha = "".join(senha_parcial)
print(f"Sua senha é: {senha}")
    