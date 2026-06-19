número = int(input("Digite um nümero para ver seu fatorial: "))
soma = 1
variável = número

for i in range(número, 0, -1):
    soma *= i 
print(f"O fatorial de {número} é {soma}")