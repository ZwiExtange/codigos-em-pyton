import os

#Operações entre inteiros
print("*** Operações entre inteiros ***")
i = 2
n = i * 2
print("i:", i, " - n:", n)
os.system("pause")
os.system("cls")

#Operações entre pontos flutuantes
print("*** Operações de divisão em ponto flutuante ***")
quo_i = int(3/2)
quo_f = 2.0/3.0
print("Resultado inteiro:", quo_i, "\nResultado flutuante:", quo_f)
os.system("pause")
os.system("cls")

print("*** Operações entre ponto flutuante ***\n")
a = 1.1
x = pow(1350.25, a); #Função intrínseca pow(): eleva-se o primeiro número à potência do segundo
print("a:", a,"\nx:", x)
os.system("pause")
os.system("cls")

#Operações entre inteiros e ponto flutuante:
print("*** Operações entre inteiros e ponto flutuante ***\n")
i = int(a)
x = x * (i + 1)
print("i:", i, "\nx:", x)
os.system("pause")
os.system("cls")

#Operações com variáveis alfanuméricas:
print("*** Atribuição com caracteres ***\n")
letra1 = "O"
letra2 = "k"
print(letra1, letra2)
os.system("pause")
os.system("cls")

#Operações aritméticas entre variáveis string não "fazem sentido" - concatenação:
print("*** Soma entre caracteres ***\n")
letras = letra1 + letra2
print("String:", letras)
os.system("pause")
os.system("cls")

#Perceba como operações aritméticas entre variáveis string não fazem sentido:
print("*** Subtração entre caracteres ***\n")
letras = letra1 - letra2
print("String:", letras)
os.system("pause")
os.system("cls")