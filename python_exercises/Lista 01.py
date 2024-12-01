# Lista para armazenar as palavras
palavras = []

# Peça 5 palavras ao usuário
for i in range(5):
    palavra = input(f"Digite a palavra {i + 1}: ")
    palavras.append(palavra)

# Contar palavras com mais de 5 letras
palavras_grandes = [palavra for palavra in palavras if len(palavra) > 5]

# Exibir a quantidade
print("Palavras com mais de 5 letras:", len(palavras_grandes))
print("Essas palavras são:", palavras_grandes)
