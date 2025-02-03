total = 0
soma = 0
n1 = 0
while n1 != 999:
    n1 = float(input('Digite um número, que será adicionado a uma sequência[digite 999 para parar]:'))
    total +=1
    if n1 != 999:
        soma += n1 
    else:
        total -=1
print(f'A quantidade de números digitados foi {total}.\n e a soma deles é {soma}')