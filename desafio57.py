sexo = input('Digite seu sexo [M/F]:').upper().strip()
while sexo == 'M'and 'F':
    sexo = input('Você digitou algo errado:')
print(f'DADOS GRAVADOS SEU SEXO É {sexo}')