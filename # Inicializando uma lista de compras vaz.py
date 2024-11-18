# Inicializando uma lista de compras vazia
lista_de_compras = []

def mostrar_lista():
    if not lista_de_compras:
        print("A lista de compras está vazia.")
    else:
        print("Lista de Compras:")
        for item in lista_de_compras:
            print("- " + item)

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Consultar lista de compras")
    print("4. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto a adicionar: ")
        lista_de_compras.append(produto)
        print(f"{produto} foi adicionado à lista de compras.")
    
    elif opcao == "2":
        produto = input("Digite o nome do produto a remover: ")
        if produto in lista_de_compras:
            lista_de_compras.remove(produto)
            print(f"{produto} foi removido da lista de compras.")
        else:
            print(f"{produto} não está na lista de compras.")
    
    elif opcao == "3":
        mostrar_lista()
    
    elif opcao == "4":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")