def alistamento_obrigatório():
    try:
        idade = int(input('Digite sua idade:'))

        if 16 < idade ==18:
            print('Você está na hora de se alistar')
        elif idade >= 45:
            print('Você não pode mais se alistar.')
        elif 45>idade>18:
            print(' Se você ainda não se alistou procure imediatemente uma brigada militar.')
        else:
            print('Você ainda não pode se alistar, espere ate completar 18 anos.')
        
    except ValueError:
        print('Você digitou algum caracter errado tente novamente.')
alistamento_obrigatório()