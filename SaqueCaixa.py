#Aqui o cliente vai se deparar com as funçoes de um caixa eletronico
saldo_total = 1000
saque = int
deposito = int
valor_atual = int

print("Escolha uma opção: ")
print("Digite 1 para Cosultar saldo: ")
print("Digite 2 para Depositar: ")
print("Digite 3 para Sacar: ")
op = int(input())

if op == 1:
    
    print("Seu saldo é: ", saldo_total)
    
    print("Deseja realizar outra operação?")
    print("Digite 10 para voltar ao menu principal")
    print("Digite 0 para Encerrar Operações")
    op = int(input())
    if op == 10:
        print("Voltar ao menu principal")
        
    if op == 0:
        print("Obrigado por ultilizar nossos Serviços")
    else:
        print("operação invalida")


elif op == 2:

    print("Digite o valor a depositar: " )
    deposito = int(input("\n"))
    valor_atual = saldo_total + deposito 
    print("Seu saldo atual é: ", valor_atual)

elif op == 3:
    saque > saldo_total = print("operação invalida")