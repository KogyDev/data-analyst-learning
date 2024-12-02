# Exercício 4: Modificando Lista
# Objetivo: Remover e substituir elementos

nomes = ["João", "Maria", "Pedro", "Ana"]

# Remova o segundo nome da lista
nomes.pop(1)

# Adicione um novo nome no lugar
nomes.insert(1, "Carlos")

print("Nova lista de nomes:", nomes)

# Exercício 5: Lista de Compras
# Objetivo: Organizar uma lista de compras

lista_compras = ["pão", "leite", "ovos"]

# Adicione mais três itens
lista_compras.extend(["queijo", "arroz", "feijão"])

# Ordene a lista de compras em ordem alfabética
lista_compras.sort()

print("Lista de compras organizada:", lista_compras)