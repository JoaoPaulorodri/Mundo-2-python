def preco_aderir():
    try:
        preco= float(input('preço da compra:R$'))
        return preco
    except ValueError:
        print('Você digitou algo de errado')
        return None

def pagamento_salvar():
    try:
        forma_pagamento=int(input('Informe forma de pagamento\n[1]à vista dinheiro/cheque\n[2]à vista cartão\n[3]3x no cartão\n[4]3x ou mais no cartão\nQual a opção?' ))
        if forma_pagamento not in [1, 2, 3, 4]:
            print('Opção inválida tente novamente')
            return None
        return forma_pagamento
    except ValueError:
        print('Você digitou algo de errado')
        return None


def main():
    preco = preco_aderir()
    if preco is None:
        return
    forma_pagamento = pagamento_salvar()
    if forma_pagamento is None:
        return
    
    if forma_pagamento == 1:
        desconto = (preco / 100) * 10
        valor_final = preco - desconto
        print(f'Sua compra será terá R${desconto:.2f} de desconto. O valor final é de R${valor_final:.2f}' )
    elif forma_pagamento ==2:
        print(f'O valor a ser pago será de R${preco}')
    elif forma_pagamento == 3:
        juros = (preco/100) * 10
        valor_final = preco + juros
        parcelas = valor_final / 2
        print(f"O valor final com o juros de R${juros:.2f} ficará em R${valor_final:.2f}")
    elif forma_pagamento == 4:
        juros = (preco/100) * 20
        valor_final = preco + juros
        parcelas = valor_final / 3
        print(f"O valor final com o juros de R${juros:.2f} ficará em R${valor_final:.2f}")
main()


