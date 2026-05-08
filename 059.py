#crie um menu de opções
from time import sleep
n1 = int(input('Digite um numero : '))
n2 = int(input('Digite outro numero : '))
opçao = 0
while opçao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opçao= int(input('Escolha sua opção: '))
    if opçao ==1 :
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é de {soma} ')
    elif opçao == 2 :
        mult= n1*n2
        print(f'{n1} X {n2} = {mult}')
    elif opçao ==3 :
        if n1 >n2 :
            maior = n1
        else:
            maior = n2
        print(f'O maior numero é {maior}')
    elif opçao == 4 :
        print("Informe novos valores:")
        n1 = int(input('Digite um numero : '))
        n2 = int(input('Digite outro numero : '))
    elif  opçao ==5 :
        print("Finalizando...")

    else:
        print('Opção invalida!')

print('='*15)
sleep(2)
print("Volte sempre!")