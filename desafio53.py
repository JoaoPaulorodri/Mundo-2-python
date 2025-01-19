frase = input('Digite uma frase:').strip().upper()
palavras = frase.split()#pega variavel frase e separa
junto = "".join(palavras)#pega as palavras e junta sem espaço
inverso = ''
for letra in range(len(junto)-1,-1,-1):#estou pegando o junto e criando uma seguencia invertida
    print(junto[letra],end='')
    inverso +=junto[letra]
if inverso == junto:
    print('\nEla é um palíndromo')
else:
    print('\nEla não é um palídromo')