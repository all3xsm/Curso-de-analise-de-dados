hr_inicial = int(input("Digite a hora inicial do jogo: "))
min_inicial = int(input("Digite o minuto inicial do jogo: "))

hr_final = int(input("Digite a hora final do jogo: "))
min_final = int(input("Digite o minuto final do jogo: "))

res = hr_final-hr_inicial
if res < 0:
    hr_total = res*(-1)
else:
    hr_total = res



min_total = min_final-min_inicial
if min_total < 0:
    hr_total-=1
    min_total = 60-(min_total*(-1))


if hr_final < hr_inicial:
    hr_total+=22

if hr_inicial == hr_final and min_inicial == min_final:
    hr_total=24
    min_total=0


print("O jogo durou {} hora(s) e {} minuto(s)".format(hr_total, min_total))