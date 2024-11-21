a= int(input('Digite um número '))
b= int(input('Digite um número '))
c= int(input('Digite um número '))

if a >= b and a >= c and b >= c:
    print('A ordem decrescente é ', a, b, c)
elif a >= b and a >= c and c >= b:
    print('A ordem decrescente é ', a, c, b)
elif b >= a and b >= c and c >= a:
    print('A ordem decrescente é ', b, c, a)
elif b >= a and c >= b and a >= b:
    print('A ordem decrescente é ', c, a, b)
elif c >= a and c >= b and b>= a:
    print('A ordem decrescente é', c, b, a)
elif b >= a and b >= c and a >= c:
    print('A ordem decrescente é', b, a, c)