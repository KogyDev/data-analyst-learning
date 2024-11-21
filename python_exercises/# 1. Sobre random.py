# 1. Sobre random.randint() e strings

# O comando random.randint(a, b) é usado para gerar números inteiros aleatórios.
# O 'a' é o valor mínimo e 'b' é o valor máximo, e ambos são inclusivos.

# Se fosse para gerar letras do alfabeto, em vez de números, usamos random.choice()
# em combinação com string.ascii_letters, string.ascii_lowercase ou string.ascii_uppercase.

import random
import string

# Exemplo: gerar uma letra aleatória do alfabeto (maiúscula ou minúscula)
letra_aleatoria = random.choice(string.ascii_letters)
print(letra_aleatoria)

# Exemplo: gerar uma string aleatória com 5 letras
letras_aleatorias = ''.join(random.choices(string.ascii_letters, k=5))
print(letras_aleatorias)

# Isso gera letras aleatórias em vez de números, sendo útil quando precisamos
# trabalhar com strings e não números inteiros.

# 2. Tentativas máximas e controle do loop

# A variável 'tentativas_maximas' define o número máximo de tentativas permitidas:
tentativas_maximas = 10

# 'tentativas' começa em 0 e vai sendo incrementada a cada palpite:
tentativas = 0

# A cada tentativa, o número de tentativas aumenta com o comando:
tentativas += 1

# O loop 'while' continua até que o número de tentativas seja igual a 'tentativas_maximas':
# Exemplo:
# while tentativas < tentativas_maximas:
# Isso significa que, se o usuário ainda tiver tentativas restantes, ele poderá continuar tentando.

# 3. Combinando 'while' e 'if/elif/else'

# O loop 'while' controla quantas vezes o código será repetido, permitindo ao usuário
# fazer novos palpites enquanto o número de tentativas for menor que o máximo.

# Se o palpite estiver errado, o código 'cai' nas condições if e elif:
# - if verifica se o palpite é menor que o número secreto.
# - elif verifica se o palpite é maior que o número secreto.
# Se nenhuma das duas condições for verdadeira, o 'else' indica que o palpite estava correto.

# Exemplo básico:
# if palpite < numero_secreto:
#     print("Seu palpite é muito baixo!")
# elif palpite > numero_secreto:
#     print("Seu palpite é muito alto!")
# else:
#     print("Parabéns! Você adivinhou o número!")

# Se o palpite for correto, usamos 'break' para sair do loop, pois o jogo acaba.

# 4. Posso usar mais de um 'elif'?

# Sim! Você pode usar quantos 'elif' forem necessários.
# Cada 'elif' permite verificar outra condição entre o 'if' e o 'else'.

# Exemplo com mais de um 'elif':
if palpite < numero_secreto - 10:
    print("Seu palpite está muito baixo!")
elif palpite < numero_secreto:
    print("Seu palpite está um pouco baixo!")
elif palpite > numero_secreto + 10:
    print("Seu palpite está muito alto!")
elif palpite > numero_secreto:
    print("Seu palpite está um pouco alto!")
else:
    print("Parabéns! Você adivinhou o número!")

# Aqui usamos várias condições para testar o quão próximo o palpite está do número secreto.

# O número de 'elif' é ilimitado, e você pode usá-los para adicionar mais verificações, dependendo das necessidades do código.
