def preco_aderir():
    try:
        preco = float(input('Preço da compra: R$'))
        return preco
    except ValueError:
        print('Você digitou algo de errado.')
        return None

def pagamento_salvar():
    try:
        forma_pagamento = int(input(
            'Informe a forma de pagamento:\n'
            '[1] À vista dinheiro/cheque\n'
            '[2] À vista cartão\n'
            '[3] 2x no cartão\n'
            '[4] 3x ou mais no cartão\n'
            'Qual a opção? '
        ))
        if forma_pagamento not in [1, 2, 3, 4]:
            print('Opção inválida. Tente novamente.')
            return None
        return forma_pagamento
    except ValueError:
        print('Você digitou algo de errado.')
        return None

def main():
    preco = preco_aderir()
    if preco is None:
        return  # Encerra o programa se o preço for inválido

    forma_pagamento = pagamento_salvar()
    if forma_pagamento is None:
        return  # Encerra o programa se a forma de pagamento for inválida

    # Cálculo e exibição do resultado
    if forma_pagamento == 1:
        desconto = (preco / 100) * 10
        valor_final = preco - desconto
        print(f'Sua compra terá R${desconto:.2f} de desconto. O valor final é de R${valor_final:.2f}.')
    elif forma_pagamento == 2:
        print(f'O valor a ser pago será de R${preco:.2f}.')
    elif forma_pagamento == 3:
        juros = (preco / 100) * 10
        valor_final = preco + juros
        parcelas = valor_final / 2
        print(f"O valor final com juros de R${juros:.2f} será de R${valor_final:.2f}, com parcelas de R${parcelas:.2f}.")
    elif forma_pagamento == 4:
        juros = (preco / 100) * 20
        valor_final = preco + juros
        parcelas = valor_final / 3
        print(f"O valor final com juros de R${juros:.2f} será de R${valor_final:.2f}, com parcelas de R${parcelas:.2f}.")

# Executa o programa principal
main()
