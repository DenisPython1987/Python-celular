
#Aqui eu crio uma saudação para o usuário
nome = "BANCO VIVAN"
print("-*-" * 20)
print(f"{nome:^60}")
print("-*-" * 20)

#Aqui eu crio uma função para criar uma conta. Eu uso um dicionário para registrar as informações
def criar_conta(nome, cpf, data_nasc):
    conta = {"nome": nome, "cpf": cpf, "data_nasc": data_nasc, "saldo": 0}
    return conta

#Eu tive que declarar a variável que viria a armazenar o cadastro de teste
usuario = 0

#Aqui eu crio o programa principal
while True:
    
    #Esse é o menu da aplicaçào
    print("""
    [ 1 ] Criar conta
    [ 2 ] Depositar
    [ 3 ] Ver saldo
    [ 4 ] Sacar
    [ 5 ] Sair""")
    
    #Aqui eu crio um tratamento de erros para garantir que só sejam digitados números
    try:
        
        #Aqui fica a entrada do usuário
        escolha = int(input("Escolha uma opção: "))
        
        #Esse if faz a validação de dados para garantir que o usuário somente digite as opções disponíveis no menu
        if escolha < 1 or escolha > 5:
            print("Opção inválida! Digite uma opção entre 1 e 5!")
            continue
            
        # Aqui eu trabalho a opção 1, que ê o cadastro de usuário. Eu crio 3 inputs para coletar o nome, CPF e data de nascimento, depois eu chamo a função "criar_conta" e insiro os dados coletados
        if escolha == 1:
            nome = str(input("Digite seu nome: "))
            cpf = str(input("Digite seu CPF: "))
            data_nasc = str(input("Digite sua data de nascimento: "))
            usuario = criar_conta(nome, cpf, data_nasc)
            
        #Aqui eu trabalho a opção 2, sobre depósito de valores
        elif escolha == 2:
            
            #Eu achei melhor criar um while para que o programa não saísse da opçào 2
            while True:
                
                #Aqui eu peço o valor do depósito
                valor = int(input("Digite o valor do depósito: R$"))
                
                #Simulando um caixa eletrônico, aqui eu garanto que o usuário só consiga sacar notas de dinheiro. O valor mínimo é de R$2,00
                if valor < 2:
                    print("Só são permitidos depósitos acima de 2 reais")
                    continue
                    
                #Simulando ainda um caixa eletrônico, eu quis garantir que não fosse possível sacar mais que 2000 reais no terminal de auto-atendimento
                elif valor > 2_000:
                    print("Depósito superior ao permitido no caixa eletrônico. Dirija-se a um guichê dentro da agência.")
                    continue
                    
                #Aqui, eu crio a condição para que o depósito seja efetivado
                elif 2 <= valor <= 2_000:
                    usuario["saldo"] += valor
                    break
                    
        #Aqui eu trabalho na opção 3, que é a consulta de saldo
        elif escolha == 3:
            print(f"O seu saldo é de R${usuario['saldo']:.2f}")
            continue
            
        #Aqui eu trabalho a opção 4, do saque. Foi a última opção que eu trabalhei e a que deu mais trabalho, onde eu errei mais
        elif escolha == 4:
            
            #Aqui eu crio while para que o programa não saísse da opção em caso de erro
            while True:
                
                #eu considerei que num caixa eletrônico não seriam disponíveis valores quebrados, por isso, eu conerti o input em int, mas não tive ideias para validar os dados caso fosse digitado um float
                saque = int(input("Digite o valor do saque: R$"))
                
                #Ainda pensando que em um terminal de auto-atendimento não se saca valor quebrado, eu determinei o valor mínimo para R$2,00 
                if saque < 2:
                    print("Valor não permitido! Digite um valor entre R$2,00 e R$2.000,00")
                    continue
                    
                #Pensando que em um banco de verdade existe um valor máximo para saque, eu determinei que esse valor é de R$2000,00
                elif saque > 2_000:
                    print(f"O valor R${saque:.2f} não pode ser sacado em um caixa eletrônico. Dirija-se a um guichê.")
                    continue
                    
                #Aqui eu criei a condição para que o valor do saque não fosse superior ao saldo
                elif saque > usuario["saldo"]:
                    print("Você não tem saldo suficiente!")
                    continue
                    
                    
                #Aqui eu crio a condição para que o saque seja efetivado
                elif 2 <= saque <= 2_000:
                    usuario["saldo"] -= saque
                    print(f"Você sacou R${saque:.2f}")
                    print(f"Seu novo saldo é de R${usuario['saldo']:.2f}")
                    break
                    
        #Aqui eu trabalho na opção de encerramento do programa
        elif escolha == 5:
            print("Obrigado por usar nossos serviços. ")
            break
    
    #Aqui eu continuo o tratamento de erros para que o valor digitado na escolha do usuário não seja uma palavra em vez de um núnero
    except ValueError:
        print("Digite apenas números entre 1 e 5. Tente novamente:")
        continue
    