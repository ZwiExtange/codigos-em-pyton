'''print("Digite um número:")
x = int(input())

print("Digite outro número:")
y = int(input())

z = x + y

print("O primeiro numero digitado foi: ", x)
print("O segundo numero digitado foi: ", y)
print("O resultado da soma é: ", z)'''


'''mat = []
soma = 0
for i in range(0, 3, 1):
    lin = []
    for j in range(0, 3, 1):
        lin.append(i + j)
    mat.append(lin)
 
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        soma = soma + mat[i][j]
 
print(soma)'''

'''a = 75
b = 150
print("Digite o valor de TBW do seu SSD sata ou nvme")
c = int(input())
d = a * c
e = b * c
print("o valor em media que seu SSD pode gravar é algo entre ", d,"Terabytes e ", e, "Terabytes que podem ser gravados")
print("A vida ultil pode variar de acordo com a gravação, e a depender da construção e da qualidade das peças")
'''
import sys
import os
def calcular_TBW():
    try:
        a = 75
        b = 150

        print("Digite o valor do TBW para saber a vida ultil de seu SSD")
        
        #Aqui vou colocar o vakor do TBW
        c = int(input("Qual o TBW do dispotivo\n"))

        #Aqui será feito o calculo interno do programa
        d = c * a
        e = c * b
        
    except ValueError:
        print("Erro, valor invalido")
        input("Aperte ''ENTER'' e o programa será encerrado e o os dados limpos.......")
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()#usado para encerrar o programa

    print("O valor em media que podem ser gravados de TBW(que é quando voce grava e apaga os dados) é um valor entre ", d, "Terabytes e ", e, "Terabytes")
    print("A vida ultil pode variar entre estes valores.")

calcular_TBW()
print(calcular_TBW)