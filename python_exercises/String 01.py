# Entrada do usuário
texto = input("Digite uma palavra ou frase: ")

# Limpar o texto removendo espaços e transformando em minúsculas
texto_limpo = texto.replace(" ", "").lower()

# Verificar se o texto limpo é igual ao seu inverso
if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
