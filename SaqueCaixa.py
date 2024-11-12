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
    valor_do_saldo = saldo_total
    print("Seu saldo atual é de:")
    print(valor_do_saldo)

    print("Ecolha uma operação:")
    print("Digite 9 para voltar ao menu anterior")
    print("Dgite 0 para ecerrar atendimento")

elif op == 2:
    deposito = int(input("Digite o valor a ser depositado: "))
    saldo_total = deposito + saldo_total
    print("Seu saldo atual é:")
    print(saldo_total)

elif op == 3:
    print("Digite o valor do saque:")
    saque = int(input())
    print("voce sacou: ", saque)
    saldo_total = saldo_total - saque
    print("Agora seu saldo atual é:")
    print(saldo_total)

else:
    print("Operação invalida")