# Por que usar float()?
# Usamos float() para garantir que o valor inserido pelo usuário não seja considerado texto (string),
# mas sim um número decimal (como 2.5, 3.75, etc.). 

# Se não fizermos isso, o valor vindo de input() será sempre tratado como texto,
# o que impede que façamos cálculos diretamente.

# No caso das notas, usamos float() porque elas podem conter casas decimais (ex.: 7.5 ou 6.75).

# Posso usar int() em vez de float()?
# Sim, você pode usar int() se souber que os valores inseridos pelo usuário serão sempre inteiros
# (números sem casas decimais, como 5, 8, etc.). int() converte a entrada para um número inteiro.

# Exemplo:
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

# O que muda ao usar int()?
# Se o usuário digitar um número com casas decimais (por exemplo, 7.5),
# o uso de int() causará um erro porque o int() só aceita números inteiros 
# ou strings que podem ser convertidas diretamente para inteiro.

# Exemplo de erro:
# Se o usuário inserir 7.5, o Python mostrará:
# ValueError: invalid literal for int() with base 10: '7.5'

# Se você estiver certo de que as notas serão inteiras (como 7, 9, 10), então int() funciona perfeitamente.
# Caso contrário, é mais seguro usar float() para permitir números com casas decimais.

# Sobre o uso de f (formatted strings)
# O uso de formatted strings (f"...") é necessário sempre que você quiser exibir 
# o valor de variáveis ou expressões dentro de um texto. 

# Isso faz com que o conteúdo do print() seja dinâmico, mudando de acordo com os inputs ou valores de variáveis.

# Quando usar f-strings:
# Sempre que você precisar exibir variáveis dentro de uma string.

# Exemplo:
nome = "Carlos"
idade = 30
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Saída:
# Meu nome é Carlos e eu tenho 30 anos.

# Se você não usar o f, a string não saberá que deve "substituir" as variáveis:
print("Meu nome é {nome} e eu tenho {idade} anos.")
# Saída:
# Meu nome é {nome} e eu tenho {idade} anos.

# Posso usar outras formas de formatação?
# Além de f-strings, existem outras maneiras de formatar strings,
# mas as f-strings são mais recomendadas por serem mais fáceis e eficientes.

# Algumas alternativas:
# Concatenando com +:
print("Meu nome é " + nome + " e eu tenho " + str(idade) + " anos.")
# Aqui, você precisa converter a variável idade para string com str().

# Usando .format():
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
# Não precisa de f, mas é menos intuitivo que f-strings.

# Conclusão:
# float(): Use quando os valores podem ter casas decimais.
# int(): Use quando os valores serão sempre inteiros.
# F-strings (f"..."): Sempre use quando quiser inserir variáveis ou resultados de cálculos dentro de uma string.
