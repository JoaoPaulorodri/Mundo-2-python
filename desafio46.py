from time import sleep  
def contagem_regressiva():
    for contagem in range(1,11):
        print(contagem)
        sleep(1.25)
print('Lançamento vai começar!')
contagem_regressiva()
print('Lançamento concluído')