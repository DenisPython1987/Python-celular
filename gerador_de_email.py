def gerador_email(lista):
    return f"{lista[0]}.{lista[-1]}@email.com"
    
def leia_nome(mensagem):
    parcial = str(input(mensagem)).strip().lower()
    final = parcial.split()
    return final
    
    
nome_lista = leia_nome("Digite seu nome: ")
email = gerador_email(nome_lista)
print(email)