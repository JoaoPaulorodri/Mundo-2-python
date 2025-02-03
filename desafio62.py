def enter_data():
    order = 1
    try:
        number = float(input('Insira o primeiro número da progressão aritmétrica:'))
        reason = float(input('Insira a razão da pa:'))
    except ValueError:
        print('Você digitou algo de errado.')
        return None
    return order , number , reason
def calculete_pa(order, number, reason):
    print(f'{number}, ', end='')
    pa = number
    mais = 10
    total= 0
    while mais !=0:
        while order < mais:
            pa +=reason
            order+=1
            total+=1
            print(f'{pa}, ', end='')
        mais = float(input('Digite quantos termos a mais:'))
        order = 0
        while order < mais:
            order+=1
            total += 1
            pa+= reason
            print(f'{pa} , ' , end='')
        
    print('fim')
    print(f'O total de pa foi de {total}')
dados = enter_data()
if dados:
    calculete_pa(*dados)