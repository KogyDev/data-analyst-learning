# Entrada do usuário
frase = input("Digite uma frase: ")

# Contar palavras
quantidade_palavras = len(frase.split())

# Contar letra "a" ou "A"
quantidade_a = frase.lower().count('a')

# Exibir em maiúsculas e minúsculas
print("Frase em maiúsculas:", frase.upper())
print("Frase em minúsculas:", frase.lower())
print("Número de palavras:", quantidade_palavras)
print("Número de vezes que a letra 'a' aparece:", quantidade_a)
