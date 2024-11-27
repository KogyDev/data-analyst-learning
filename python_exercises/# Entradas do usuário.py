# Entradas do usuário
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar na frase: ")

# Verificar se a palavra está na frase
if palavra in frase:
    print(f"A palavra '{palavra}' está na frase.")
else:
    print(f"A palavra '{palavra}' NÃO está na frase.")
