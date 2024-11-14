#aqui o cliente vai se deparar com as funcoes de um caixa eletronico
saldo_total = 1000

while True:
    print("SEJA BEM VINDO AO BANCO \n")
    print("1 para Consultar Saldo")
    print("2 para Saque")
    print("3 para Deposito")
    print("0 para Encerrar")
    op = int(input("DIGITE A OPERAÇÃO A REALIZAR: \n"))

    if op == 1:
        print("Seu saldo atual é R$ ")
        print(saldo_total)

    elif op == 2:
        print("Quanto voce quer sacar? \n")
        print("Notas disponiveis para saque")
        print("100, 50, e 20")
        saque = int(input())
        
        if saque > saldo_total:
            print("Saldo insuficiente")
            if saque < 20:
                print("Saque minimo de R$ 20")

        else:
            saldo_total -= saque
            print("voce sacou R$: ", saque)
            print("Agora seu saldo atual é:", saldo_total)


    elif op == 3:
        print("Qual o valor a depositar?")
        deposito = int(input())
        saldo_total = deposito + saldo_total
        print("Voce depositou R$ ", deposito)
        print("Agora seu saldo em R$ atual é: ", saldo_total)

    elif op == 0:
        print("Atendimento ecerrado")
        print("Obrigado por usar nossos serviços")
        break
    else:
        print("operação invalida")
