#Váriaveis Python

# O que é uma variável?
# Uma variável é como uma caixa onde você armazena um valor (um número, um texto, etc.) para usar depois no seu código.
# Cada variável tem um nome que você escolhe, e o valor dentro dela pode mudar ao longo do programa.

# Como declarar uma variável?
# Em Python, declarar uma variável é super simples. Você só precisa dar um nome para ela e atribuir um valor usando o símbolo =:
nome = "Carlos"
idade = 25

# Aqui:
# nome é uma variável que guarda o valor "Carlos".
# idade é uma variável que guarda o valor 25.

# Regras para nomes de variáveis
# Os nomes de variáveis podem ser quase qualquer coisa, mas seguem algumas regras:
# Não pode começar com números. Exemplo: 1nome (inválido).
# Não pode conter espaços. Use o underline (_) para separar palavras. Exemplo: primeiro_nome.
# Não pode usar palavras reservadas da linguagem (como if, while, etc.).
# Case sensitive: O Python diferencia maiúsculas de minúsculas. Então Nome e nome são variáveis diferentes.

# Tipos de Variáveis
# Em Python, você não precisa declarar o tipo da variável (como em algumas linguagens). O Python detecta automaticamente o tipo, de acordo com o valor que você atribui.

# Aqui estão alguns tipos comuns:
# int (inteiros): Números sem casa decimal.
idade = 25

# float (números decimais): Números com casa decimal.
altura = 1.75

# str (strings): Textos, ou qualquer valor entre aspas (simples ou duplas).
nome = "Carlos"

# bool (booleanos): Valores lógicos, como True ou False.
ativo = True

# Mudança de Valor
# O valor de uma variável pode ser alterado durante a execução do programa. Por exemplo:
x = 10
x = 20  # Agora, x vale 20

# Operações com Variáveis
# Você pode fazer operações com variáveis, dependendo do tipo delas. Exemplos:
# Números:
a = 5
b = 3
soma = a + b  # soma será 8

# Texto (strings): Com strings, o símbolo + serve para concatenar (juntar) textos.
primeiro_nome = "Carlos"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome  # Resultado: "Carlos Silva"

# Conversão de Tipos
# Às vezes, você precisa converter uma variável de um tipo para outro. Por exemplo, se você pegar um número como texto e quiser somá-lo com outro número. Para isso, você pode usar funções como int(), float(), ou str().
idade_str = "25"  # É uma string
idade_int = int(idade_str)  # Converte para inteiro

altura = 1.75
altura_str = str(altura)  # Converte para string

# Variáveis e Tipos Mistas
# Se tentar misturar variáveis de tipos diferentes de forma errada, você pode receber erros. Exemplo:
nome = "Carlos"
idade = 25
# print("Meu nome é " + nome + " e eu tenho " + idade + " anos.")  # Isso gera um erro.

# Para resolver, você pode converter o número em string:
print("Meu nome é " + nome + " e eu tenho " + str(idade) + " anos.")

# Atribuições em Cadeia
# Você pode atribuir o mesmo valor a várias variáveis de uma vez:
a = b = c = 10  # a, b e c terão o valor 10

# Atribuições Incrementais
# Você pode modificar o valor de uma variável em função do valor atual:
contador = 10
contador += 1  # contador agora é 11
contador *= 2  # contador agora é 22
# Isso é equivalente a:
contador = contador + 1
contador = contador * 2
