n1= int(input('Digite sua 1º nota:'))
n2= int(input('Digite sua 2º nota:'))
nota= (n1 + n2) / 2
print("Nota media: ", nota)

if nota >= 7 and nota < 10:
    print('Você foi Aprovade!')
elif nota >= 10:
    print("Você foi aprovade com distinção, hora de uma revisão para a próxima")
else:
    print('Infelizmente você foi reprovade, good luck next time')