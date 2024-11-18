numero = int(input("Digite qualquer numero inteiro: "))

resto = int(numero / 2)
resto = numero - resto * 2

if resto == 1:
    print("O numero é impar")

else:
    print("O numero é par")