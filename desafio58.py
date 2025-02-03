import random
print('Sou seu computador, acabei de pensar em um número entre 0 a 10')
itens = [0,1,2,3,4,5,6,7,8,9,10]
escolha_computador= random.randint(0,10)

minha_escolha=int(input('Tente adivinhar:'))
while escolha_computador != minha_escolha:
    minha_escolha=int(input('Você perdeu escolha outro numero'))
    if escolha_computador == minha_escolha:
        print('Parabéns você ganhou')
        break
print(f'O computador escolheu {escolha_computador}')
