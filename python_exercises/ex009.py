a= int(input('Digite o primeiro valor: '))
b= int(input('Digite o segundo valor: '))
c= int(input('Digite o terceiro valor: '))
maior = a
if b > a and b > c:
    maior = b
    print('O menor número digitado foi: ', a or c)
    print('O maior número digitado foi: ', b)
elif c > a and c > b:
    maior = c
    print('O menor número digitado foi: ', a or b)
    print('O maior número digitado foi: ', c)

    menor = a

elif b < a and b < c:
    menor = b
    print('O menor número digitado foi ', b)
    print('O maior número digitado foi ', a or c)
elif c < a and c < b:
    menor = c
    print('O menor número digitado foi ', c)
    print('O maior número digitado foi ', a or b)

