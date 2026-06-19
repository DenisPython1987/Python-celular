cpf = input("Digite o CPF: ")
cpf_split = cpf.split()
lista = []
números = [10, 9, 8, 7, 6, 5, 4, 3, 2]
soma_1 = 0
digito_1 = 0
validade = 0
for i in cpf_split:
    lista.append(int(i))
    
for i in range(1, 10):
    mult = lista[i] * números[i]
    soma_1 += mult

if soma_1 % 11 < 2:
    digito_1 = 0
else:
    digito_1 = 11 - soma_1

if digito_1 == lista[9]:
    validade += 1

print(validade)