import random
contador = 0
vitorias=0 
derrotas =0
vencedor=0

while True:
    par_impar = str(input('Par ou impar:')).upper()
    minha_escolha = float(input('digite um número de 0 a 9:'))
    escolha_computador= random.randint(0,9)
    soma = minha_escolha + escolha_computador
    if par_impar=='PAR' and soma %2 ==0:
            par_impar = 'PAR'
            vitorias += 1
    elif par_impar == 'IMPAR' and soma % 2 !=0 :
            par_impar ='IMPAR'
            vitorias +=1
    elif par_impar == 'PAR' and soma % 2 == 1:
        par_impar = 'IMPAR'
        derrotas +=1
    elif par_impar == 'IMPAR' and soma % 2 == 0:
        par_impar = 'PAR'
        derrotas +=1
    print(f' Você escolheu {minha_escolha}, o computador {escolha_computador}, a soma é {minha_escolha + escolha_computador}, o resultado é {par_impar}')
    if derrotas == 3:
        vencedor = 'computador'
        print(f'O vencedor foi o {vencedor}')
        break
    if vitorias ==3:
         vencedor = 'jogador'
         print(f'O vencedor foi o {vencedor}')
