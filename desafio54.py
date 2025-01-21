def inserir_nomes():
    try:
        n1 = int(input('Digite o ano de aniversário da primeira pessoa:'))
        n2 = int(input('Digite o ano de aniversário da segunda pessoa:'))
        n3 = int(input('Digite o ano de aniversário da terceira pessoa:'))
    except ValueError:
        print('Você digitou algo além de número')
        return None
    return  n1 , n2 , n3

def determinar_maioridade(n1,n2,n3):
    ano_atual = 2025
    idades = [ano_atual - n for n in (n1, n2, n3)]
    totalmaior = 0
    totalmenor = 0
    for i, idade in enumerate(idades, start=1):
        if idade >= 18:
            print(f'A pessoa {i} é maior de idade com {idade} anos.')
            totalmaior +=1

        else:
            print(f'A pessoa {i} é menor de idade com {idade} anos.')
            totalmenor +=1
    print(f' foram {totalmaior} pessoas maior de idade e {totalmenor} pessoas menor de idade') 

dados = inserir_nomes()
if dados:
    determinar_maioridade(*dados)


