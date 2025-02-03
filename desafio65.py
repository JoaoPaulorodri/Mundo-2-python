maior = 0
menor = 0
total = 0
soma = 0
media = 0
continuacao = 0
while continuacao != 'N' :
    numero = float(input('Digite um número:'))
    continuacao = str(input('Quer continuar? [S/N]: ')).upper()
    total += 1
    soma += numero
    if total == 1:
        maior = menor = numero
    else:
       if numero > maior:
            maior = numero
       if numero < menor:
            menor = numero
media = soma / total
print(f'A soma dos números é {soma}, o total de números digitados é {total} ')
print(f'O maior é {maior},o menor é {menor} ')
print(f'A média é {media}')
