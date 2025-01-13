def categoria_base():
    try:
        ano = int(input('Digite o ano de nascimento:'))
        idade = 2025 - ano

        if idade <= 9:
            print('Sua categoria:mirim')
        elif 9 < idade <= 14:
            print('Sua categoria:infantil')
        elif 14 < idade <= 19 :
            print('Sua categoria: junior ')
        elif idade == 20 and 19:
            print('Sua categoria é sênior')
        else:
            print('Sua categoria:Master')

    except ValueError:
        print('Você digitou algo errado')
categoria_base ()