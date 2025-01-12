def comparar_numeros():
    try:
        n1 = float(input('Digite um número:'))
        n2 = float(input('Digite outro número:'))
        if n1 > n2:
            print(f'O primeiro número {n1} é maior do o segundo {n2}. ')
        elif n2 > n1 :
            print(f'O segundo número {n2} é maior que o primeiro {n1}')
        else:
            print('O dois são iguais')
    except ValueError:
        print('Você digitou algo errado:')
comparar_numeros()
