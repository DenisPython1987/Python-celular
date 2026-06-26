from math import sqrt

while True:
    saudação = "SOLUCIONADOR DE EQUAÇÃO DO 2° GRAU"
    print("\033[35m-*-" * 20)
    print(f"{saudação:^50}")
    print("-*-" * 20)
    print("\033[m")
    
    try:
        a = float(input("\033[32mDigite o coeficiente A: \033[m"))
        b = float(input("\033[32mDigite o coeficiente B: \033[m"))
        c = float(input("\033[32mDigite o coeficiente C: \033[m"))
    
    except ValueError:
        print("\033[31mValor inválido! Digite um número real ou inteiro!\033[m")
        continue
    discriminante = (b ** 2) - (4 * a * c) 

    if discriminante < 0:
        print("\033[36mNão existem raízes reais!\033[m")
    elif discriminante >= 0:
        x_1 = (-b + sqrt(discriminante)) / (2 * a)
        x_2 = (-b - sqrt(discriminante)) / (2 * a)
        print(f"\033[36mA raiz x' é {x_1:.2f} e a raiz x'' é {x_2:.2f}\033[m")
    escolha = str(input("\033[32mQuer continuar? [ S / N ]:  \033[m")).strip().upper()[0]
    if escolha not in "SsNn":
        print("\033[31mEscolha inválida! Tente novamente.\033[m")
        escolha = str(input("\033[32mQuer continuar? [ S / N ]: \033[m")).strip().upper()[0]
    if escolha in "Nn":
        break

print("\033[36mAgradecemos por usar nosso programa. Volte sempre!\033[m")