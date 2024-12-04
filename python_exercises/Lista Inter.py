# Exercício: Sistema de Gerenciamento de Notas de Turma

# Lista de dicionários representando alunos e suas notas
alunos = [
    {"nome": "Ana", "notas": [7.5, 8.0, 6.5], "idade": 17},
    {"nome": "Carlos", "notas": [6.0, 5.5, 7.0], "idade": 16},
    {"nome": "Maria", "notas": [9.0, 8.5, 9.5], "idade": 18},
    {"nome": "Pedro", "notas": [4.5, 5.0, 4.0], "idade": 17},
    {"nome": "Juliana", "notas": [8.5, 9.0, 8.0], "idade": 16}
]

def calcular_media(notas):
    """Calcula a média das notas de um aluno"""
    return sum(notas) / len(notas)

def classificar_desempenho(media):
    """Classifica o desempenho do aluno"""
    if media >= 9:
        return "Excelente"
    elif media >= 7:
        return "Bom"
    elif media >= 5:
        return "Regular"
    else:
        return "Insuficiente"

# Processamento das notas
resultados = []
for aluno in alunos:
    media = calcular_media(aluno["notas"])
    resultado = {
        "nome": aluno["nome"],
        "media": round(media, 2),
        "desempenho": classificar_desempenho(media),
        "passou": media >= 6
    }
    resultados.append(resultado)

# Ordenar resultados da maior média para a menor
resultados_ordenados = sorted(resultados, key=lambda x: x["media"], reverse=True)

# Imprimir resultados
print("===== BOLETIM DA TURMA =====")
for resultado in resultados_ordenados:
    print(f"Nome: {resultado['nome']}")
    print(f"Média: {resultado['media']}")
    print(f"Desempenho: {resultado['desempenho']}")
    print("Situação: Aprovado" if resultado['passou'] else "Situação: Reprovado")
    print("---")

# Estatísticas gerais
medias = [resultado["media"] for resultado in resultados]
print("\n===== ESTATÍSTICAS =====")
print(f"Média geral da turma: {round(sum(medias) / len(medias), 2)}")
print(f"Melhor média: {max(medias)}")
print(f"Pior média: {min(medias)}")
print(f"Total de aprovados: {sum(1 for resultado in resultados if resultado['passou'])}")
print(f"Total de reprovados: {sum(1 for resultado in resultados if not resultado['passou'])}")