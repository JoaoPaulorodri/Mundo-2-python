def corverte_número():
    try:
        n1 = int(input('Digite um número inteiro:'))
        print('Escolha uma das opções para conversão:\n[1] converter para binário\n[2] converter para octal\n[3] converter para hexadecimal')
        opção = int(input('Sua opção:'))
        if opção == 1:
            print(f'Em binário {bin(n1)}')
        elif opção == 2:
            print(f'Em binário {oct(n1)}')
        else:
            print(f'Em hexadecimal {hex(n1)}')
    except ValueError:
        print('Você digitou algo de errado')

corverte_número()