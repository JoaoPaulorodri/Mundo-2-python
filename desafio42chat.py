def entrada_segmentos():
    """Solicita ao usuário os valores dos três segmentos e retorna como uma lista."""
    try:
        r1 = float(input('Digite o valor do primeiro segmento: '))
        r2 = float(input('Digite o valor do segundo segmento: '))
        r3 = float(input('Digite o valor do terceiro segmento: '))
        return r1, r2, r3
    except ValueError:
        print("Erro: Você deve digitar apenas números.")
        return None

def forma_triangulo(r1, r2, r3):
    """Verifica se os segmentos podem formar um triângulo."""
    return r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2

def tipo_triangulo(r1, r2, r3):
    """Determina o tipo de triângulo formado pelos segmentos."""
    if r1 == r2 == r3:
        return "Equilátero"
    elif r1 == r2 or r1 == r3 or r2 == r3:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    """Função principal que coordena a execução do programa."""
    segmentos = entrada_segmentos()
    if segmentos is None:
        return

    r1, r2, r3 = segmentos

    if forma_triangulo(r1, r2, r3):
        print("Com esses valores é possível criar um triângulo.")
        tipo = tipo_triangulo(r1, r2, r3)
        print(f"O triângulo formado é do tipo: {tipo}.")
    else:
        print("Com esses valores não é possível formar um triângulo.")

# Executa o programa
if __name__ == "__main__":
    main()
