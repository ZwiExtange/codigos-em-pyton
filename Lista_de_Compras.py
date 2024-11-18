#LISTA DE COMPRAS
lista_compras = []

while True:
    print("Bem Vindo a sua Lista de Compras particular")
    print("Aqui voce pode adicionar e remover itens, conforme querer\n")

    print("Digite 1 para adicionar um item")
    print("Digite 2 para remover um item")
    print("Digite 3 para ver a lista de compras")
    print("Digite 0 para sair")

    op = input("Digite a opção que deseja: ")

    if op == "1":       #Comparar como string
        item = input("Digite o nome do item que deseja adicionar: ")        #Solicita o item ao usuario
        lista_compras.append(item)      #Adiciona o item a lista
        print(f"{item} foi adicionado à lista.")
    
    elif op == "2":
        if not lista_compras:       #Verificando se a lista está vazia
            print("A lista de compras está vazia. Não há itens para remover.")
        else:
            print("Escolha o item que deseja remover")
            for i in range(len(lista_compras)):
                print(f"{i + 1} - {lista_compras[i]}")
            item = int(input("Digite o número do item que deseja remover: "))
            if 1 <= item <= len(lista_compras):     #Aqui vai verificar se o numero esta dentro do intervalo
                removed_item = lista_compras.pop(item - 1) #Aqui remove o item
                print(f"{removed_item} foi removido da lista")
            else:
                print("Numero invalido. Nenhum item doi removido")

    elif op == "3":
        if not lista_compras:       #Aqui verifica se a lista esta vazia
            print("A lista está vazia.")
        else:
            print("Lista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i} - {item}")

    elif op == "0":
        print("Obrigado por usar nossos serviços")
        print("Esperamos de te ver novamente")
        print("Caso precise adicionar, remover ou consultar usa lista de compras só voltar aqui novanente")
        break

    else:
        print("Operação invalida")
