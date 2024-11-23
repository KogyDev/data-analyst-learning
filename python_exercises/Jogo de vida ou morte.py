# Jogo simples de vida ou morte
escolha = input("Você escolhe a vida ou a morte? (digite 'vida' ou 'morte'): ").lower()

if escolha == 'vida':
    print("Você vive para lutar outro dia!")
elif escolha == 'morte':
    print("Você sucumbe ao destino... Game over!")
else:
    print("Escolha inválida! Tente novamente.")
