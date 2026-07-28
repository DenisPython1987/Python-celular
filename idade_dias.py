from Utilidades.números import leia_int
from datetime import date

hoje = date.today().year
ano_nasc = leia_int("\033[36mDigite seu ano de nascimento: \033[m")
idade = hoje - ano_nasc
dias = idade * 365
print(f"\033[33mVocê tem {idade} anos, que em dias são {dias}.\033[m")