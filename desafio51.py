def inserir_dados():
    try:
        n1 = int(input('Digite o primeiro número:'))
        razao = int(input('digite a razão:'))
        
    except ValueError:
        print('Você digitou algo de errado')
        return None
    return n1 , razao

def progressao_executar(n1 , razao):
    termos = []
    for repeticao in range(10):
        termos.append(str(n1))
        n1 += razao
    print(', '.join(termos))
    
dados = inserir_dados()
progressao_executar(*dados)