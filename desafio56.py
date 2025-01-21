def inserir_dados():
   somaidade = 0
   somamulheres20 = 0
   nome_maisvelho = ''
   idade_maisvelho = 0
   try:
        for c in range(1,5):
            print(f'-----{c} PESSOA-----')
            nome = input('Nome:')
            idade = int(input('IDADE:'))
            sexo = input('SEXO [M/F]:').upper()
            somaidade += idade
            if sexo == "F" and idade <= 20:
                    somamulheres20 +=1
            if sexo == 'M' and (idade > idade_maisvelho or c== 1):
                    idade_maisvelho = idade
                    nome_maisvelho = nome
            
            media_idade = somaidade/4
   except ValueError:
        print('Você digitou algo errado')
   return nome_maisvelho, idade_maisvelho, somamulheres20, media_idade
def mostrar_analises(nome_maisvelho, idade_maisvelho, somamulheres20, media_idade):
    print(f' A media de idades é {media_idade}.\nO homem mais velho tem {idade_maisvelho} e seu nome é {nome_maisvelho}.\nA quantdade mulheres com vinte ou menos é {somamulheres20}')

dados = inserir_dados()
mostrar_analises(*dados)
