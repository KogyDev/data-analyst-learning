# Loop para fazer o cálculo de várias notas
while True:
    # Solicita a nota do aluno
    nota = float(input("Digite a nota do aluno (0 a 10): "))

    # Classificação baseada na nota usando 'elif'
    if nota >= 9:
        print("Excelente!")
    elif nota >= 7:
        print("Bom!")
    elif nota >= 5:
        print("Médio!")
    else:
        print("Reprovado!")

    # Pergunta ao usuário se ele deseja continuar
    continuar = input("Deseja calcular a nota de outro aluno? (sim/não): ").lower()
    
    # Se a resposta não for 'sim', o loop vai parar
    if continuar != "sim":
        print("Obrigado por usar a calculadora de notas!")
        break
