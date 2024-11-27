# Função para codificar uma mensagem
def codificar(mensagem, deslocamento):
    nova_mensagem = ""
    for letra in mensagem:
        if letra.isalpha():  # Se for uma letra
            base = ord('A') if letra.isupper() else ord('a')  # Maiúscula ou minúscula
            nova_letra = chr((ord(letra) - base + deslocamento) % 26 + base)
            nova_mensagem += nova_letra
        else:
            nova_mensagem += letra  # Mantém espaços e pontuação
    return nova_mensagem

# Entrada do usuário
mensagem = input("Digite a mensagem para codificar: ")
deslocamento = int(input("Digite o valor do deslocamento (chave): "))

# Codifica e exibe o resultado
mensagem_codificada = codificar(mensagem, deslocamento)
print("Mensagem codificada:", mensagem_codificada)
