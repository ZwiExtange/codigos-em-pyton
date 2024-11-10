num1 = float(input("Digite o primeiro numero: \n"))
num2 = float(input("Digite o segundo numero: \n"))

print("Escolha uma operação: ")
print("Digite 1 para somna;")
print("Digite 2 para subtração")
print("Digite 3 para Multiplicação")
print("Digite 4 para Divisão")
op = int(input())

if op == 1:
    resultado = num1 + num2
    print("A Soma é: ", resultado)
elif op == 2:
    resultado = num1 - num2
    print("A Subtração é: ", resultado)
elif op == 3:
    resultado = num1 * num2
    print("A Multiplicação é: ", resultado)
elif op == 4:
    resultado = num1 / num2
    print("A divisão é: ", resultado)
else:
    print("Operação Invalida.")
