total = 0
produto_mil = 0
maisbarato = None
contagem = 0
while True:
    nome_produto = str(input('DIGITE O NOME DO PRODUTO:'))
    preco = float(input('Digite o preço do produto:'))

    if maisbarato is None or preco < maisbarato :
        maisbarato = preco
    if preco >= 1000:
        produto_mil += 1
   


    continuar = input('Quer continuar?[S/N]').upper()
    
    
    total +=preco
    contagem +=1

    
    if continuar  not in('s', 'S', 'n' ,'N'):
        print('Você digitou algo errado.Tente novamente')
        continue
    elif continuar == 'N' :
        break
    
    
   
   
    
    

print(f'O total foi de R${total:.2f}.\nTemos {produto_mil} produtos custando 1000 ou mais.\n O produto mais barato custa {maisbarato}')

