# Operadores em Python
# Operadores são símbolos usados para realizar operações com variáveis e valores. Eles podem ser aritméticos, de comparação, lógicos, entre outros.

# Operadores Aritméticos
# Usados para realizar operações matemáticas.

a = 10
b = 3

# Soma (+)
resultado = a + b  # Resultado: 13

# Subtração (-)
resultado = a - b  # Resultado: 7

# Multiplicação (*)
resultado = a * b  # Resultado: 30

# Divisão (/)
resultado = a / b  # Resultado: 3.333 (resultado é sempre um float)

# Divisão Inteira (//)
resultado = a // b  # Resultado: 3 (a parte inteira da divisão)

# Módulo (%) 
# Retorna o resto da divisão
resultado = a % b  # Resultado: 1 (resto da divisão de 10 por 3)

# Potenciação (**)
resultado = a ** b  # Resultado: 1000 (10 elevado à potência de 3)

# Operadores de Comparação
# Usados para comparar valores e retornam True ou False.

# Igual (==)
resultado = (a == b)  # False

# Diferente (!=)
resultado = (a != b)  # True

# Maior que (>)
resultado = (a > b)  # True

# Menor que (<)
resultado = (a < b)  # False

# Maior ou igual (>=)
resultado = (a >= b)  # True

# Menor ou igual (<=)
resultado = (a <= b)  # False

# Operadores Lógicos
# Usados para combinar condições. Retornam True ou False.

x = True
y = False

# AND (e)
resultado = x and y  # False (só é True se ambos forem True)

# OR (ou)
resultado = x or y  # True (só é False se ambos forem False)

# NOT (não)
resultado = not x  # False (inverte o valor, True vira False e vice-versa)

# Operadores de Atribuição
# Usados para atribuir valores às variáveis e podem incluir operações.

c = 10

# Atribuição simples (=)
c = 10  # A variável c recebe o valor 10

# Atribuição com soma (+=)
c += 5  # Equivale a c = c + 5 (c agora vale 15)

# Atribuição com subtração (-=)
c -= 3  # Equivale a c = c - 3 (c agora vale 12)

# Atribuição com multiplicação (*=)
c *= 2  # Equivale a c = c * 2 (c agora vale 24)

# Atribuição com divisão (/=)
c /= 4  # Equivale a c = c / 4 (c agora vale 6.0)

# Atribuição com divisão inteira (//=)
c //= 2  # Equivale a c = c // 2 (c agora vale 3)

# Atribuição com módulo (%=)
c %= 2  # Equivale a c = c % 2 (c agora vale 1)

# Atribuição com potenciação (**=)
c **= 3  # Equivale a c = c ** 3 (c agora vale 1)

# Operadores de Identidade
# Verificam se duas variáveis apontam para o mesmo objeto na memória.

d = [1, 2, 3]
e = d

# is
resultado = (d is e)  # True (apontam para o mesmo objeto)

# is not
resultado = (d is not e)  # False (não são objetos diferentes)

# Operadores de Pertinência
# Verificam se um valor está em uma sequência (lista, string, etc.).

frutas = ["maçã", "banana", "laranja"]

# in
resultado = "maçã" in frutas  # True (maçã está na lista frutas)

# not in
resultado = "uva" not in frutas  # True (uva não está na lista frutas)
