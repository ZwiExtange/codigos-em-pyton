
def caixa_eletronico():
    valor_do_caixa = 1500
    
    try:
        saque = int(input("Digite o valor a sacar: "))

        if saque > valor_do_caixa:
            print("Operação invalida")
            return None
        else:
            print("Saque valido")
            print("Voce sacou")
            print(saque)
            valor_do_caixa -= saque
            print("Voce possui agora na conta: ", valor_do_caixa)
            return saque
    
    except ValueError:
        print("Por favor, insira um valor valido.")

while True:
    
    caixa_eletronico()


#include <windows.h>
#include <stdio.h>

int main(){
    printf("Searching for problems....\n");
    Sleep(60000);
    printf("We dind't find any problems \n");
}