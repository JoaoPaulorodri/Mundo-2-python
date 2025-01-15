def calcular_imc():
    try:
        peso = float(input('Digite seu peso:'))
        altura = float(input('Digite seu altura:'))
        imc = peso/ (altura **2)
        print(f'O imc da pessoa é {imc:.2f}')
        if 25<=imc<=30:
            print('Você está com sobrepeso')
        elif 30<= imc <=40:
            print('Você está com obesidade')
        elif imc > 40:
         print('Você está com obesidade mórbida')
        elif imc < 18.5:
           print('Você está abaixo do peso')
        else:
           print('Você está com o peso ideal')
    except ValueError:
       print('Você digitou algo errado')

calcular_imc()