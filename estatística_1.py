

funcionário = dict()

def apresentação(mensagem):
    """Função para apresentação de cabeçalhos. Aceita como parâmetro a mensagem a ser apresentada"""
    print("-*-" * 20)
    print(f"{mensagem:^60}")
    print("-*-" * 20)
    
def verifica_int(mensagem):
    """Função para validar números inteiros. Aceita como parâmetro a mensagem quanto à natureza do valor"""
    while True:
        try:
            número = int(input(mensagem))
            return número
        except ValueError:
            print("Dado inválido! Digite apenas números inteiros.")
            continue
            
def continuar():
    """Função para perguntar ao usuário se ele quer continuar utilizando o programa. Não aceita parâmetros. Retorna 'S' ou 'N'"""
    while True:
        try:
            escolha = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
            if escolha not in "SN":
                print("Opção inválida! Digite somente S ou N!")
                continue
            if escolha in "SN":
                return escolha
        except IndexError:
            print("Sua opção não pode ficar vazia")
            continue

def validar_data(data_str):
    """
    Função para validar datas. recebe uma data em formato de string."""
    from dateutil.parser import parse, ParserError
    try:
        parse(data_str)
        return True
    except (ParserError, ValueError, TypeError):
        return False
        
def calcular_idade(data_nascimento):
    """Função para calcular a idade da pessoa. Recebe como parâmetro uma data em formato de string. Retorna a idade da pessoa."""
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    nascimento = datetime.strptime(data_nascimento, "%d%m%Y")
    hoje = datetime.now()
    diferença = relativedelta(hoje, nascimento)
    return diferença.years

while True:
    apresentação("Cadastro de Funcionários")
    nome = str(input("Digite o nome do funcionário: ")).strip().title()
    funcionário['nome'] = nome
    while True:
        data_nascimento = str(input("Digite a data de nascimento do funcionário [dd/mm/aaaa]: ")).strip()
        validação_nascimento = validar_data(data_nascimento)
        if not validação_nascimento:
            print("Data inválida! digite um ano válido.")
            continue
        if validação_nascimento:
            idade = calcular_idade(data_nascimento)
            funcionário['data_nascimento'] = data_nascimento
            if idade >= 16:
                funcionário['idade'] = idade
    escolha_principal = continuar()
    if escolha_principal == "N":
        break
print(funcionário)
    