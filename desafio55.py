def inserir_peso():
    pesos = []
    try:
        for p in range(1,4):
            peso =[float(input('Digite o peso:'))]
            pesos.append(peso)
    except ValueError:
        print('Você digitou algo inválido.')
        return None
    return pesos
    
def maior_menor(pesos ):
  maior = max(pesos)
  menor = min(pesos)
  print(f'O mairo peso é {maior}KG e o menor {menor}KG')
dados = inserir_peso()
if dados:
    maior_menor(dados)