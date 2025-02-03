tamanho = int(input('Quantos termos:'))
order = 3
first = 0
second = 1
third = first + second
print(f'{first}, {second}, ' , end='')
print(f'{third}, ',end='')
while order <= tamanho:
    order+=1
    first = second
    second = third
    third = first + second
    print(f'{third}, ', end='')
print('fim')