mat = []

for i in range(3):
    linha = []
    for j in range(3):
        print("Insira o elemento da linha", i, "coluna", j)
        dado = int(input())
        linha.append(dado)
    mat.append(linha)

for i in range(3):
    for j in range(3):
        print("O elemento da linha", i, "coluna ", j, "é:", mat[i][j])




'''#JA NO COMANDO FOR É USADO PARA QUANDO VOCE PRECISA DE ALGO MAIS PRECISO E QUE SE NECESSARIO PRECISE ALTERNAR NUMEROS
cont = int

for cont in range(11):
    print("contando de 0 a 10")
    print(cont)
#ACIMA TEMOS UMA ESTRUTURA SIMPLIFICADA'''
#AGORA ABAIXO TEMOS UMA ESTRUTURA QUE ESPECIFICA E ABRANGE MAIS POSSIBILIDADES USANDO O MESMO CODIGO
'''cont = int

print("Conte até 10 apartir de 1 bilhao")
for cont in range(1,1000000000,1):
    print(cont)
#Aqui ele vai contar até 1 bilhao
'''


'''#NOVOS COMANDO WHILE
#No comando While é usado para repetição
nome = input("Digite seu nome aqui: ")

i = 0
while i < 10:
    print("Seu nome será repetido 10x", nome)
    i  += 1'''


'''#TESTE DO COMANDO DE TESTES NOTAS POR MEIO DO SITEMA DE "IF" e "ELSE"

print("Sistema de notas das provas dos alunos")
media = float(input("Digite aqui a nota do aluno: "))

if media >= 7:
    print("Aprovado")
else:
    if media >= 4:
        print("Tem direito a SUB")
    else:
        media < 4
        print("Reprovado")
#ESTE COMANDO ACIMA É PARA UM SISTEMA DE NOTAS'''




'''#AGORA NO É PRECISO PRATUICAR OUTRO CODIGO QUE SERIA UM SISTEMA DE OPCOES TAMBEM USANDO O SISTEMA IF E ELSE COM INCLUSAO DO ELIF
#COMADNOS USADOS """ELIF, IF e ELSE"
num1 = int(input("Digite um numero qualquer inteiro: \n"))
num2 = int(input("Digite o segundo numero qualquer inteiro: \n"))

print("Digite uma das opcoes abaixo: ")
print("Digite 1 para a soma")
print("Digite 2 para subtração")
print("Digite 3 para divisão")
print("Digite 4 para multiplicação")
op = int(input())

if op == 1:
    resultado = num1 + num2
    print("A soma é igual a: ", resultado)

elif op == 2:
    resultado = num1 - num2
    print("O resultado da subtração é: ", resultado)

elif op  == 3:
    resultado = num1 / num2
    print("O resultado da divisão é: ", resultado)

elif op == 4:
    resultado = num1 * num2
    print("O resultado da multiplicação é: ", resultado)

else:
    print("opção invalida")'''


