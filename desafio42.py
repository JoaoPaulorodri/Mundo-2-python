r1 = float(input('Digite o valor de um segmento:'))
r2 = float(input('Digite o valor de outro segmento:'))
r3 = float(input('Digite o valor de um terceiro segmento:'))
def triangulo_determinar():
    try:
        if r1< r2 + r3 and r2< r1 + r3 and r3 < r1+ r2:
            print('Com esses valores é possivel criar um triângulo')
        else:
            print('Com esses valores não é possível criar um triângulo')
    except ValueError:
        print('Você digitou algo errado.')
triangulo_determinar()  

def tipo_triangulo():
    if r1< r2 + r3 and r2< r1 + r3 and r3 < r1+ r2 and r1 == r2 ==r3 :
        print('O triangulo é equilatero')
    elif r1< r2 + r3 and r2< r1 + r3 and r3 < r1+ r2 and r1 == r2 !=r3:
        print('O triangulo é isóceles')
    else:
        print('Triangulo é escaleno')
tipo_triangulo()