# Aqui o cliente vai se deparar com as funções de um caixa eletrônico
saldo_total = 1000

while True:  # Loop para manter o menu ativo
    print("\nEscolha uma opção: ")
    print("Digite 1 para Consultar saldo: ")
    print("Digite 2 para Depositar: ")
    print("Digite 3 para Sacar: ")
    print("Digite 0 para Encerrar atendimento")
    
    op = int(input())

    if op == 1:
        print("Seu saldo atual é de:")
        print(saldo_total)

    elif op == 2:
        deposito = int(input("Digite o valor a ser depositado: "))
        saldo_total += deposito
        print("Seu saldo atual é:")
        print(saldo_total)

    elif op == 3:
        saque = int(input("Digite o valor do saque: "))
        if saque > saldo_total:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldo_total -= saque
            print("Você sacou: ", saque)
            print("Agora seu saldo atual é:")
            print(saldo_total)

    elif op == 0:
        print("Atendimento encerrado.")
        break  # Sai do loop e encerra o programa

    else:
        print("Operação inválida")