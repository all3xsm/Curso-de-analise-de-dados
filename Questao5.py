def calculaSalario(salario_bruto):
    desconto_inss = salario_bruto - (salario_bruto * 0.11)
    salario_liquido = desconto_inss - (desconto_inss * 0.15)

    return salario_liquido

salario_bruto = float(input('Digite o valor bruto do seu salário: '))

print('Seu salário líquido é no valor de {}'.format(calculaSalario(salario_bruto)))