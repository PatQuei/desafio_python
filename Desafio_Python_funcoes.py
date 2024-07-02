print('='*30)
print('{:^30}'.format("PatBank"))
print('='*30)

def menu():
    menu = """\n 
===============MENU===============
[1] Depositar
[2] Saque
[3] Extrato
[4] Nova conta
[5] Listar contas
[6] Novo Usuário
[7] Sair


=> """
    return menu

def depositar(saldo, extrato, valor_deposito, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: \tR$ {valor_deposito:.2f}\n"
        print ("Depósito realizado, com sucesso!")
    else:
        print('='*30)
        print('{:^30}'.format("Falha ao depositar, valor digitado inválido!"))
        print('='*30)

    return saldo, extrato

def sacar(*,valor_saque, limite_saques, limite, saldo, extrato):
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
        print('='*30)
        print('{:^30}'.format("Saque realizado com sucesso!"))
        print('='*30)
        numero_saques += 1
    else:
        print('{:^30}'.format("O valor do saque deve ser maior que 0."))

    return saldo, extrato

def exibir_extrato (saldo, / , *, extrato):
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: \tR${saldo:.2f}")
        print('='*30)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário existente")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF:")
    usuarios = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print('='*30)
        print("\n Conta criada com sucesso!")
        print('='*30)
        return {"agencia":agencia, "numero_conta":numero_conta, "usuarios":usuarios}
    
    print("\n Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
        print("=" * 100)
        print(linha)

def main():

    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    limite_saques = 3
    numero_saques = 0
    usuarios = []
    contas = []



    while True:
        print(menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print('='*30)
            print('{:^30}'.format("DEPÓSITO"))
            print('='*30)
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, extrato, valor_deposito)

                
        elif opcao == "2":
            print('='*30)
            print('{:^30}'.format("SAQUE"))
            print('='*30)
            valor_saque = float(input("Digite o valor de retirada: "))
            saldo, extrato = sacar (
                valor_saque = valor_saque, 
                limite_saques = limite_saques, 
                limite = limite, 
                saldo = saldo, 
                extrato = extrato
            )

        elif opcao == "3":
            print('='*30)
            print('{:^30}'.format("EXTRATO"))
            print('='*30)
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            numero_conta = criar_conta(agencia, numero_conta, usuarios)
            if numero_conta:
                contas.append(numero_conta)


        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)
	
        elif opcao == "7":
            break

        else: 
            print('='*30)
            print('{:^30}'.format("Opção inválida! Tente novamente."))
            print('='*30)



if __name__ == "__main__":
    main()