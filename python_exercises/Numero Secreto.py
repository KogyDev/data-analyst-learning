import random

# O computador escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# O jogador tem 3 tentativas
tentativas = 3

while tentativas > 0:
    # Pede para o jogador fazer uma tentativa
    tentativa = int(input(f"Você tem {tentativas} tentativas. Qual número você acha que o computador escolheu? "))
    
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break  # Sai do loop se o jogador acertar
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    
    tentativas -= 1

else:
    print(f"Fim de jogo! O número secreto era {numero_secreto}.")
