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