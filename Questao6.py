def valorPagamento(prestacao, dias_atraso):

    contas = 0
    total = 0

    while(True):

        if dias_atraso == 0:
            valor_pagar = prestacao
        
            print('O valor a ser pago é de: {}'.format(valor_pagar))
            contas+=1
            total+=valor_pagar

            prestacao = float(input('Digite o valor da prestação: '))
            if prestacao == 0:
                break
            dias_atraso = int(input('Digite o número de dias em atraso: '))
            
    
        elif dias_atraso != 0:
            multa = prestacao + (prestacao * 0.03)
            multa_total = multa + ((dias_atraso * 0.001) * prestacao)
            valor_pagar = multa_total

            print('O valor a ser pago é de: {}'.format(valor_pagar))
            contas+=1
            total+=valor_pagar

            prestacao = float(input('Digite o valor da prestação: '))
            if prestacao == 0:
                break
            dias_atraso = int(input('Digite o número de dias em atraso: '))
            

    print('A quantidade de prestações pagas foi de {} e o total é de {}'.format(contas,total))

prestacao = float(input('Digite o valor da prestação: '))
dias_atraso = int(input('Digite o número de dias em atraso: '))

valorPagamento(prestacao, dias_atraso)
