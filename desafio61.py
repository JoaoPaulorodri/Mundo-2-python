def enter_data():
    order = 0
    try:
        number=float(input('Digite o primeiro número da PA:'))
        reason = float(input('Digite a razão da PA:'))

    except ValueError:
        print('Você digitou algo além de número')
        return None
    return number , reason, order
def calculete_pa(number, reason, order):
    print(f'{number}, ', end='')
    pa = number
    while order < 10:
       order += 1
       pa += reason
       print(f'{pa} , ',end='')

data = enter_data()
if data:
    calculete_pa(*data)
print('fim')