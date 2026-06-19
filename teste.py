def validacao(nota):
    if 0 > nota or nota > 10:
        print(f"A nota {nota} está fora do intervalo permitido. Digite uma nota de 0 à 10. Tente novamente!")
        return 1

saudacao = 'AVALIAÇÃO FINAL'
print("-=-" * 20)
print(f'{saudacao:^80}')
print("-=-" * 20)
        
aluno = str(input('Qual é o nome do aluno(a)?         ')).strip().title()

while True:
   
    nota_1 = float(input('Digite a primeira nota: '))
    controle = validacao(nota_1)
    if controle == 1:
        continue
    nota_2 = float(input('Digite a segunda nota: '))
    controle = validacao(nota_2)
    if controle == 1:
        continue
    nota_3 = float(input('Digite a terceira nota: '))
    controle = validacao(nota_3)
    if controle == 1:
        continue
    nota_4 = float(input('Digite a quarta nota: '))
    controle = validacao(nota_4)
    if controle == 1:
        continue
    break
    
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"A média do(a) aluno(a) {aluno} é {media:.2f}")

if media < 6:
    print(f"O(a) aluno(a) {aluno} está REPROVADO!")
elif media < 9.9:
    print(f"O(a) aluno(a) {aluno} está APROVADO!")
elif media == 10:
    print(f"O(a) aluno(a) {aluno}foi aprovado com louvor!")