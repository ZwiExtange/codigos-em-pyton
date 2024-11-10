def soma(num1, num2, total):
    total.append(num1 + num2)
    

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

resultado = []

soma(n1, n2, resultado)

print("A soma é: ", resultado[0])
#para alteração de dados mutaveis ou nao mutaveis


#novamente este codigo abaixo é um exemplo de codigos mutaveis ou nao mutaveis
def soma(num1, num2):
    num1 = num1 + num2
    return num1

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero"))

resultado = soma(n1, n2)

print("A soma é: ", resultado)


'''
#ESCOPOS DA FUNÇÃO

#Função global vs Local
#FUNÇÃO GLOBAL

raio = 0

def areaTriangulo():
    return 3.14*raio**2

raio = float(input("Digite o raio do triangulo: "))

area = areaTriangulo()

print("A area do triangulo é: ", area)


#Agora a mesma função so que versao LOCAL
#FUNÇÃO LOCAL

def areaTriangulo(r):
    return 3.14*r**2

raio = float(input("Digite o raio do triângulo: "))

area =  areaTriangulo(raio)

print("A área do triangulo é: ", area)

'''


'''def soma(num1, num2):
    total = num1 + num2
    return total

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

resultado = soma(n1, n2)

print("A soma é", resultado)
'''



'''
#uso da função "def"
def soma():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    total = num1 + num2
    print("A soma é", total)

soma()
'''

'''#Agora sobre matrizes
mat = []

mat.append([1, 2, 3])
mat.append([4, 5, 6])
mat.append([7, 8, 9])

print(mat[0][0])
print(mat[2][2])
print(mat[0][2])
print(mat[1][0])
'''


'''#linhas de codigo usadas principalmente para que se possa tornar maisculas e minusculas e ver como ficariam
#usado os novos codigos "len", ".upper", ".lower"
nome = input("Digite seu primeiro nome: \n ")
sobrenome = input("Digite seu sobrenome: \n")

tamanho = len(nome)
print("O comprimento do nome é: ", tamanho)

nome = nome +""+ sobrenome
print("Após concectar as strings temos: ", nome)

if sobrenome in nome:
    print("O sobrenome ", sobrenome, "está contido no nome ", nome, ".")

print("O nome completo minusculo é: ", nome.lower())
print("O nome completo maiusculo é: ", nome.upper())
'''


'''import os
#quando voce quiser saber qual o numero de uma determinada posição use o seguinte comando:
lista = [10, 20, 30, 40, 50]

print("Lista preenchida: ", lista)

print("Acessando o ultimo elemento (-1): ", lista[-1])
print("Acessando o penultimo elemento (-2): ", lista[-2])

print("Testando o acesso da poisção com o -3: ", lista[-3])

input("Aperte qualquer tecla para limpar: ")

os.system("cls")
'''

'''#uso dos comandos "append" e "pop"
#fazendo substituiçoes nos numeros
lista = [10, 20, 30]

print(lista)

lista [1] = 99
#lembrando que como a contagem começa em "0" entao o numero colocado 1 sera o segundo na ordem da linha
print(lista)
'''



'''
#Adicionando numeros e removendo o ultimo numero com comandos
lista = [10, 20, 30]
print("Lista original: ", lista)

lista.append(99) #vai ser usado para adicionar o numero na ultima posicao em ordem final
print("Adicionando o 99:", lista)

aux = lista.pop()
print("Elemento removido: ", aux)

print("Resultado final: ", lista)
'''


'''mat = []

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

'''

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


