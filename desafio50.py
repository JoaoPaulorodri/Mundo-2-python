def numeros_inteiros():
    try:
        n1 = int(input('Digite um número inteiro:'))
        n2 = int(input('Digite um número inteiro:'))
        n3 = int(input('Digite um número inteiro:'))
        n4 = int(input('Digite um número inteiro:'))
        n5 = int(input('Digite um número inteiro:'))
        n6 = int(input('Digite um número inteiro:'))
    except ValueError:
        print('Você digitou algo além de um número')
    ## essa função vai retornar um tupla 
    return n1 , n2, n3, n4, n5,n6 

def soma_numeros(n1 , n2, n3, n4, n5, n6):
    total = 0
    for c in [n1 , n2, n3, n4, n5, n6]:
        if c %2 == 0:
            total = total+ c
    print(f'A soma dos números pares é {total}')

numeros = numeros_inteiros()
soma_numeros(*numeros)  # Usa o operador * para descompactar os valores
## descompacta a tupla para que cada numero seja executado por vez
#tupla é uma coleção denúmeros que sempre e executada todas de uma vez, * faz com que cada numero seja lido um por vez