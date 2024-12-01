# Crie uma lista vazia
numeros = []

# Peça 5 números ao usuário
for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Some todos os números
soma = sum(numeros)

# Exiba o resultado
print("A soma dos números é:", soma)
