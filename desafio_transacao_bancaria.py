print('='*30)
print('{:^30}'.format("PatBank"))
print('='*30)

menu = """ 
[1] Depositar
[2] Saque
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print('='*30)
        print('{:^30}'.format("DEPÓSITO"))
        print('='*30)
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print('='*30)
            print('{:^30}'.format("Depósitos só são aceitos \n com valor acima de 0."))
            print('='*30)
                
    elif opcao == "2":
        print('='*30)
        print('{:^30}'.format("SAQUE"))
        print('='*30)
        valor_saque = float(input("Digite o valor de retirada: "))
        if valor_saque > saldo:
            print('='*30)
            print('{:^30}'.format("Saldo insuficiente."))
            print('='*30)
        elif valor_saque > limite:
            print('='*30)
            print('{:^30}'.format("O valor de saque excede o \n limite permitido."))
            print('='*30)
        elif numero_saques >= limite_saques:
            print('='*30)
            print('{:^30}'.format("Número máximo de saques \n diários excedido."))
            print('='*30)
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print('{:^30}'.format("O valor do saque deve ser maior que 0."))

    elif opcao == "3":
        print('='*30)
        print('{:^30}'.format("EXTRATO"))
        print('='*30)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Seu saldo é de R${saldo:.2f}")
        print('='*30)
	
    elif opcao == "4":
        break

    else: 
        print('='*30)
        print('{:^30}'.format("Opção inválida! Tente novamente."))
        print('='*30)