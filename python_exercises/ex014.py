valor_hora = float(input('Digite o valor da hora de trabalho '))
quant_hora_trabalhada = float(input('Digite a quantidade de hora trabalhada '))

salariob = valor_hora * quant_hora_trabalhada
fgts = (salariob * 11) / 100
sind = (salariob * 3) / 100

if salariob <= 900:
        salariol = salariob - sind

elif salariob > 900 and salariob <= 1500:
        ir = (salariob *5) / 100
        salariol = salariob - sind - ir

elif salariob > 1500 and salariob <= 2500:
        ir = (salariob * 5) / 100
        salariol = salariob - ir - sind

else:
        ir = (salariob * 20) / 100
        salariol = salariob - ir - sind


        print('Seu salario bruto é: %7.2f' % salariob)
        print('O valor do seu FGTS é de:  %7.2f' % fgts)
        print('O sindicato vai te levar: %7.2f'% sind)
        print('O desconto do IR foi de: ¨%7.2f' % ir)
        print('Seu salario liquido é de: %7.2f' % salariol)
