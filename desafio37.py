def corverte_número():
    try:
        n1 = int(input('Digite um número inteiro:'))
        
    except ValueError:
        print('Você digitou algo de errado')