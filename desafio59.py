def enter_data():
    try:
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Insira o segundo número:'))
        operation = int(input('[1]SOMAR\n[2]multiplicar\n[3]maior\n[4]novos números\nDigite a sua escolha: '))
        if operation == 4:
             n1 = float(input('Digite o primeiro número:'))
             n2 = float(input('Insira o segundo número:'))
             operation = int(input('[1]SOMAR\n[2]multiplicar\n[3]maior\n[4]novos números\nDigite a sua escolha: '))
        elif operation > 4:
            print('Digitou uma opção inválida')
            return None
    except ValueError:
        print('Você digitou algo inválido')
        return None
    return n1, n2 , operation
def calculate_respond(n1,n2, operation):
    if operation == 1:
        sum = n1 + n2
        print(f'A soma de {n1} e {n2} é {sum}')
    elif operation == 2:
        multiplication = n1 * n2
        print(f' A MULTIPLICAÇÃO ENTRE {n1} E N2{n2} é {multiplication}')
    elif operation == 3:
        if n1 > n2:
            print(f'O maior número é {n1}.')
        elif n1 < n2:
            print(f'O maior número é {n2}')
        else:
            print('Os números são iguais')
data = enter_data()
if data:
    calculate_respond(*data)
    
