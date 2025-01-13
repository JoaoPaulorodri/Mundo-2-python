def ler_notas ():
    try:
        nota1 = float(input('Digite a primeira nota:'))
        nota2 = float(input('Digite a segunda nota:'))

        media = (nota1 + nota2) /2

        if media < 5:
            print(f'Você não atingiu a média esperada de 5.0 pontos. Sua média foi de {media}. Você foi reprovado')
        elif 5 <= media <= 6.9:
            print(f' Sua média é de {media}.Você está de recuperação')
        else:
            print(f'Sua média é de {media}.Parabéns você foi aprovado')
    except ValueError:
        print('Você digitou algo errado.')
ler_notas()