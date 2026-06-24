idade = soma = cont = maior_homem = maior_mulher = 0
cadastro = {}
homem_mais_velho = mulher_mais_velha = ""
while True:
    while True:
        nome = str(input("Digite o nome: ")).strip().lower()
        if nome.isdigit():
            print(f"{nome} não é um nome válido. Tente novamente.")
            continue
        elif not any(char.isalnum() for char in nome):
            print(f"{nome} não é um nome válido. Tente novamente!")
            continue
        elif nome in "@#$_&-+()/?!;:*£~|•√π÷×§∆\\}{=°^¥€¢%©®™✓[]<>":
            print("Seu nome não pode conter caracteres especiais. Digite um nome válido.")
            continue
        else:
            break

    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0 or idade > 125:
                print("Idade inválida. Tente novamente!")
                continue
            else:
                soma += idade
                break
        except ValueError:
            print(f"{idade} não corresponde a uma idade válida. Tente novamente!")
            continue

    while True:
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
        if sexo not in "MmFf":
            print("Sexo inválido. Tente novamente")
            continue
        if sexo in "MmFf":
            break
    cadastro[nome] = {"nome": nome, "idade": idade, "sexo": sexo}
    cont += 1
    if cont == 1:
        maior_mulher = idade
        maior_homem = idade
    if idade > maior_mulher and sexo in "Ff":
        maior_mulher = idade
        mulher_mais_velha = nome
    if idade > maior_homem and sexo in "Mm":
        maior_homem = idade
        homem_mais_velho = nome
    escolha = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]
    
    if escolha in "Nn":
        média = soma / cont
        break

print(f"Ao todo, foram {cont} cadastros.")
print(f"A soma das idades é {soma} anos.")
print(f"A média de idade é de {média} anos.")
print(f"O homem mais velho tem {maior_homem} anos e se chama {homem_mais_velho.title()}")
print(f"A mulher mais velha tem {maior_mulher} anos e se chama {mulher_mais_velha.title()}")
