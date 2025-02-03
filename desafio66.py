total = soma = 0

while True:
    numero = float(input('Digite um valor [digite 999 para parar]:'))
    total +=1
    if numero == 999:
        break
    soma += numero 
    
print(f'A soma dos {total} números é {soma}')