# Função global
numeros = []  # Lista global

def adicionar_numero(num):
    """Função local para adicionar um número à lista global."""
    numeros.append(num)  # Adiciona o número à lista

def soma():
    """Função local para calcular a soma dos números na lista."""
    total = 0
    for num in numeros:
        total += num
    return total

def main():
    # Variáveis de diferentes tipos
    continuar = True  # Bool
    nome = input("Qual é o seu nome? ")  # String
    print(f"Bem-vindo, {nome.upper()}!")  # Usando upper()

    while continuar:
        # Solicita um número ao usuário
        numero = float(input("Digite um número (ou digite -1 para sair): "))  # Float

        if numero == -1:
            continuar = False  # Para sair do loop
        else:
            adicionar_numero(numero)  # Chama a função para adicionar o número

    # Exibe a soma dos números
    print(f"A soma dos números digitados é: {soma()}")  # Chama a função soma()

    # Exibe a lista de números
    print(f"Números digitados: {numeros}")  # Lista
    print(f"Quantidade de números digitados: {len(numeros)}")  # Usando len()

    # Exibe o resto da divisão de um número
    if len(numeros) > 0:
        resto = numeros[-1] % 2  # Resto da divisão do último número por 2
        print(f"O resto da divisão do último número por 2 é: {resto}")

# Chama a função main
if __name__ == "__main__":
    main()