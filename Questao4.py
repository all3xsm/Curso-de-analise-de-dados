lista = []

while True:
    dados = int(input('Digite sua idade: '))

    if dados < 0:
        print('A media é: {}'.format((sum(lista) / len(lista))))
        break
    
    lista.append(dados)