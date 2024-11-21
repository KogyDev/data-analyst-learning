primeiro= int(input('Primeiro Numero : '))
segundo= int(input('Segundo Numero : '))
terceiro= int(input('Terceiro Numero : '))

if primeiro > segundo and terceiro:
    print('O primeiro número é o maior: ', primeiro)
elif segundo> primeiro and terceiro:
    print('O segundo número é o maior: ', segundo)
elif terceiro> primeiro and segundo:
    print('O terceiro número é o maior: ', terceiro)
