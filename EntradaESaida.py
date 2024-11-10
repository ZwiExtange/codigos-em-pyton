x = 9999
y = 111.18391
z = 1500000000000000000

#Imprimindo uma mensagem simples (stdout):
print("Mensagem a ser exibida na tela.\n")

#Imprimindo o conteúdo de variáveis:
print("Conteúdo da variável x: ")   #Texto simples
print(x)					        #Conteúdo de variável inteira
print("\n")	 					    #Quebra de linha: 2x

#Misturando a impressão entre texto e conteúdo de variáveis:
print("Conteúdo da variável y:", y)

#Formatando o número de casa decimais de um ponto flutuante:
print(f"Variável y formatada para uma casa decimal: {y:.1f}")

#Formatando a impressão de um número flutuante para a notação científica:
print(f"Conteúdo da variável z: {z:e}\n\n")

#Lendo valores do teclado:
print("Digite um valor inteiro: ")
x = int(input())

print("Digite um valor numérico com casas decimais: ")
y = float(input())

print("\nOs valores digitados foram:", x, "e", y)
