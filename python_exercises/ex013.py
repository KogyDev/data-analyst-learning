salario = float(input('Salário do Colaborador: '))
if(salario <= 280):
    percentual = 20

elif(salario <= 700):
    percentual = 15

elif(salario <= 1500) :
    percentual = 10

else:
    percentual = 5

print('Salario original: R$ ', salario)
print('Percentual: ', percentual, '%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('Aumento: R$ ', aumento)
print('Novo Salário: R$', novo_salario)