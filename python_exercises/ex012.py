turno = input('Digite o turno em que você estuda: D = Diurno, V = Vespertino, N = Noturno: ')
if turno == 'D' or turno == 'd':
    print('Bom dia, seja bem-vinde')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde, seja bem-vinde')
elif turno == 'N' or turno == 'n':
    print('Boa Noite, durma bem')
else:
    print('Valor inválido :^( ')