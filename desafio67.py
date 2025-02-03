while True:
    numero = float(input('Digite o número da tabuada:'))
    if numero < 0:
        break
    for i in range(0,11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')
print('Programa encerrado')