def gerar_tabuada():
    try:
        n1 =int(input('Digite um número:'))
        if n1 is None:
            return
        if 1<= n1 <=10:
            for tabuada in range(1,11):
                print(f'{n1} x {tabuada} = {n1 * tabuada}')
    except ValueError:
        print('Você digitou algo errado')

gerar_tabuada()