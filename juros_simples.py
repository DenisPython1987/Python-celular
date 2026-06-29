
while True:
    try:
        capital = float(input("\033[35mQual é o capital inicial? \033[m"))
        if capital < 1:
            print("\033[31mO capital não pode ser negativo! Tente novamente.\033[m")
            continue
        if capital > 0:
            break
    except (ValueError, TypeError):
        print("\033[31mDado inválido! Tente novamente!\033[m")
        continue

while True:
    try:      
        taxa = float(input("\033[35mQual é a taxa? [em decimal]: \033[m"))
        if taxa < 0:
            print("\033[31mA taxa não pode ser negativa! Tente novamente.\033[m")
            continue
        if taxa > 0:
            break
    except (ValueError, TypeError):
        print("\033[31mDado inválido! Tente novamente!\033[m")
        continue

while True:
    try:
        tempo = int(input("\033[35mPor quanto tempo? \033[m"))
        if tempo < 0:
            print("\033[31mO tempo não pode ser negativo! Tente novamente.\033[m")
            continue
        if tempo > 0:
            break
    except (ValueError, TypeError):
        print("\033[31mDado inválido! Tente novamente!\033[m")
        continue
        
juros = (capital * taxa) * tempo
montante = capital + juros

print(f"\033[36mOs juros são: {juros:.2f}.\033[m")
print(f"\033[36mO montante é: {montante:.2f}.\033[m")