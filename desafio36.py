def autorizar_emprestimo():
    try:
        valor_casa = float(input('Qual o valor da sua casa? '))
        salário = float(input('Qual o seu salário:'))
        parcelas = valor_casa / 50
        procentagem_salario = (salário / 100) * 30
        
        if parcelas <= procentagem_salario:
            print(f'Empréstimo aprovado!\nAs parcelas serão de R${parcelas}.')
        else:
            print(f' Empréstimo negado!\nValor das parcelas de {parcelas} excede a 30 por cento do seu salário de R${salário} ')
        
    except ValueError:
        print('Você digitou algo de errado.')
autorizar_emprestimo()