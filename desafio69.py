mulheres= 0
homens = 0
adultos =0
menos_20 =0
while True:
    sexo = str(input('Sexo[M/F]')).upper()
    idade= int(input('Idade:'))
    continuar = str(input('Quer continuar?[s/n]:')).upper()
    #adicionar contadores
    if sexo == 'F':
        mulheres +=1
        if idade < 20:
            menos_20 +=1
    elif sexo == 'M':
        homens +=1
    elif idade >= 18 : 
        adultos +=1 
    #instalar o break
    if continuar == 'N':
        break
print(f'O número de mulheres é {mulheres}.\nO de mulheres com menos de 20 anos é {menos_20}.\nO número de homems é {homens}.\n O número de adultos é {adultos} ')