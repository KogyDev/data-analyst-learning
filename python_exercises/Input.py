#Input 

# 1. O que é o input()?

# A função input() é usada para capturar dados inseridos pelo usuário via teclado.
# O valor inserido é sempre retornado como string.

# Exemplo básico:
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

# 2. Conversão de tipos de dados

# O input() sempre retorna uma string. Para trabalhar com números, você precisa convertê-los.
# Para inteiros, usamos int(), e para números decimais, usamos float().

# Exemplo de conversão para inteiro:
idade = int(input("Quantos anos você tem? "))
print(f"Você tem {idade} anos.")

# Exemplo de conversão para float:
altura = float(input("Qual é a sua altura em metros? "))
print(f"Sua altura é {altura} metros.")

# 3. Validação de entrada (try/except)

# Para evitar erros quando o usuário insere um valor inválido (por exemplo, texto em vez de número),
# podemos usar try e except para capturar o erro e pedir para o usuário tentar novamente.

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break  # Sai do loop se o valor for válido
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# 4. Captura de múltiplas entradas (usando split)

# Se quiser capturar mais de um valor em uma única linha, podemos usar split().
# O split divide a string inserida com base em espaços (ou outros separadores).

nome, idade = input("Digite seu nome e idade separados por um espaço: ").split()
idade = int(idade)  # Convertendo idade para número inteiro
print(f"Seu nome é {nome} e você tem {idade} anos.")

# 5. Exemplo completo com validação

# Aqui está um exemplo completo combinando validação de entrada para números inteiros e decimais.

nome = input("Digite seu nome: ")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Erro: por favor, insira um número inteiro válido.")

while True:
    try:
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))
        break
    except ValueError:
        print("Erro: por favor, insira um número decimal válido.")

print(f"Seu nome é {nome}, você tem {idade} anos e sua altura é {altura} metros.")
