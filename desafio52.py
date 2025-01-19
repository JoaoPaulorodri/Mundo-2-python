def inserir_numero():
    try:
        numero = int(input('Digite um número:'))
    except ValueError:
        print('Você digitou algo de errado')
        return None
    return numero

def determinar_divisores(numero):
    divisores = []
    for divisor in range(1,numero +1 ):
        if numero % divisor == 0:
            divisores.append(divisor)
    return divisores

dado = inserir_numero()
if dado :
    divisores = determinar_divisores(dado)
    print(f' Os divisores de {dado} são:{", ".join(map(str, divisores))}')
