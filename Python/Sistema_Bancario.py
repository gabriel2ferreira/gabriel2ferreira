#Constante do sistema 
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
#Variáveis a serem utilizadas
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
#While para fazer o sistema rodas indefinidamente 
while True:

    #Chama o menu para ser impresso em tele e recebe comando
    opcao = input(menu)

    #deposito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    #saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        #verifica se o valor de saque é maior que o saldo
        excedeu_saldo = valor > saldo

        #verifica se o valor é maior que o limite
        excedeu_limite = valor > limite

        #verifica a quantidade de saques
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        #realiza o saque e conta o numero de saques
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")