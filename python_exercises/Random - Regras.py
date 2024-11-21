# 1. O que é o `random`?
# O módulo `random` é usado para gerar valores aleatórios, como números, escolhas aleatórias
# de listas e até mesmo embaralhar elementos. 

# 2. Como importar o `random`?

# Importação completa do módulo
import random

# Importando funções específicas (exemplo: randint e choice)
from random import randint, choice

# 3. Funções comuns do `random`:

# Gera um número inteiro aleatório entre dois valores (inclusive)
numero_aleatorio = random.randint(1, 100)

# Escolhe um item aleatório de uma lista
cores = ['vermelho', 'azul', 'verde']
cor_aleatoria = random.choice(cores)

# Embaralha uma lista (altera a lista original)
cartas = ['A', 'K', 'Q', 'J']
random.shuffle(cartas)

# Gera um número float entre 0.0 e 1.0
numero_float = random.random()

# Gera um número float entre a e b
numero_uniforme = random.uniform(1.5, 7.5)

# 4. Problemas comuns com `random`:

# - Certifique-se de sempre importar o módulo no início:
# import random

# - Não nomeie variáveis como 'random', pois isso sobrescreve o módulo:
# random = 5  # Isso causa erro, evite!

# - Use tipos de dados corretos nos parâmetros das funções:
# Por exemplo, `random.randint(1, 10)` exige dois inteiros.

# 5. Exemplo para uso no jogo da cobrinha:

# Gerar coordenadas aleatórias para a comida no jogo da cobrinha
tamanho_jogo = 20
comida_x = random.randint(0, tamanho_jogo - 1)
comida_y = random.randint(0, tamanho_jogo - 1)

print(f"A comida apareceu nas coordenadas: ({comida_x}, {comida_y})")
