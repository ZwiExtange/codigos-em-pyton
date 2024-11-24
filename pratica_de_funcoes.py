lista = []

def imprime():
    for freelancer in lista:
        print("**** Código do freelanccer:", freelancer["cod"])
        print("Nome:", freelancer["nome"])
        print("E-Mail:", freelancer["email"])
        print("Linguagem:", freelancer["linguagem"])
        print("Preço por hora (R$):", freelancer["valor"])
        print("-------------------")

def menu():
    print("-------------    FRELANCERS - VERSÃO BETA   -------------")
    print("1 - Digite 1 para inserir novo cadastro de freelancer;")
    print("2 - Digite 2 para mostrar freelancers cadastrados;")
    print("0 - Digite 0 para encerrar.")

cont = 0
op = -1

while op != 0:
    menu()
    op = int(input())

    if op == 1:
        if len(lista) < 5:
            freelancer = {}

            freelancer["cod"] = cont
            freelancer["nome"] = input("Insira o nome do freelancer: \n")
            freelancer["email"] = input("Insira o e-mail do freelancer: \n")
            freelancer["linguagem"] = input("Insira a principal liguagem de programação do freelancer:  \n")
            freelancer["valor"] = float(input("Insira o preço do freelancer por hora  trabalhada (R$): \n"))

            lista.append(freelancer)
            cont += 1
        else:
            print("Lista de freelancers lotada")
        input("Pressione Enter para continuar...")
    elif op == 2:
        if not lista:
            print("Lista de freelancers vazia!")
        else:
            imprime()
            input("Pressione Enter para continuar...")
    elif op != 0:
        print("Erro: opção invalida!")
        input("Pressione Enter para continuar...")