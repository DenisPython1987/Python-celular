from Utilidades.números import leia_float, leia_int, moeda
from Utilidades.cores import cor_aleatória, cor_final

def dividir(valor, pessoas):
    return valor / pessoas
    
def percentual(valor, percento):
    return (percento / 100) * valor

cor_aleatória()
valor_geral = leia_float("Quanto vocês gastaram? R$")
cor_final()
cor_aleatória()
qnt_pessoas = leia_int("Em quantas pessoas vocês estão? ")
cor_final()
cor_aleatória()
valor_garçon = leia_float("Qual é o percentual do garçon? ")
cor_final()
perct_garçon = percentual(valor_geral, valor_garçon)
valor_geral += perct_garçon
valor_todos = dividir(valor_geral, qnt_pessoas)
cor_aleatória()
print(f"O valor para {qnt_pessoas} pessoas é {moeda(valor_todos)}")
cor_final()
cor_aleatória()
print(f"O percentual do graçon é {moeda(perct_garçon)}")
cor_final()