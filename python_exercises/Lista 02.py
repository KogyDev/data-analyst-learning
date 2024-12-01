# Lista para armazenar os números
numeros = []

# Peça 10 números ao usuário
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Filtrar os números pares
pares = [num for num in numeros if num % 2 == 0]

# Exiba os números pares
print("Os números pares são:", pares)
