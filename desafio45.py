from random import randint
def minha_escolha():
    try:
        itens = ('papel','tesoura','pedra')
        escolha = int(input('Escolha um\n[0]papel\n[1]tesoura\n[2]pedra\nSua escolha: '))
        if escolha  not in [0,1,2]:
            print('Você digitou algo de errado')
            return None
        print(f'Você escolheu {itens[escolha]}')
        return escolha
        
    except ValueError:
        print('Você digitou algo de errado')
        return None
def computador_escolher():
    itens = ('papel', 'tesoura','pedra')
    computador_choice = randint(0,2)
    print(f'Computador escolheu {itens[computador_choice]}')
    return computador_choice

def main():
    computador_choice = computador_escolher()

    escolha=minha_escolha()
    if escolha is None: 
        return 
    
    if escolha == computador_choice:
        print(f'EMPATE! ')
    elif (escolha == 0 and computador_choice == 2) or \
         (escolha == 1 and computador_choice == 0) or \
         (escolha == 2 and computador_choice == 1):
        print('Você ganhou')
    else:
        print('Você perdeu')
if __name__ == "__main__":
    main()