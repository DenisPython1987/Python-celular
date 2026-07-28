from Utilidades.números import leia_int
from Utilidades.escolha_continuar import continuar

candidato_1 = candidato_2 = 0
while True:
    print("""\033[35m
        Você quer votar em:
         [ 1 ] - Candidato 1
         [ 2 ] - Candidato 2\033[m""")
    voto = leia_int("\t\033[36mSeu voto: (1 ou 2): \033[m")
    if voto < 1 or voto > 2:
        print("\033[31mNúmero inválido. Digite apenas um ou dois.\033[m")
        continue
    if voto == 1:
        candidato_1 += 1
    if voto == 2:
        candidato_2 += 1
    escolha = continuar()
    if escolha == "N":
        break
        
if candidato_1 > candidato_2:
    print(f"\033[33mCandidato 1 ganhou a eleição com {candidato_1} votos.\033[m")
if candidato_1 < candidato_2:
    print(f"\033[33mCandidato 2 ganhou a eleição com {candidato_2} votos.\033[m")
if candidato_1 == candidato_2:
    print("\033[33mTivemos um empate.\033[m")