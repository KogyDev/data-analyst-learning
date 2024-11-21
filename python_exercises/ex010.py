p1 = int(input('Digite o preço do primeiro item: '))
p2 = int(input('Digite o preço do segundo item: '))
p3 = int(input('Digite o preço do terceiro item: '))

menor = p1

if p1 < p2 and p1 < p3:
    print ('O primeiro item é o mais barato, compre ele!')
elif p2 < p1 and p2 < p3:
    print ('O segundo item é o mais barato, compre agora!')
elif p3 < p1 and p3 < p2:
    print('O terceiro item é o mais barato, compre-o imediatamente')


