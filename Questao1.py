pares = 0

for i in range(5):
    valores = int(input('Digite o valor: '))
    if valores % 2 == 0:
        pares+=1

print('A quantidade de par(es) é: {}'.format(pares))