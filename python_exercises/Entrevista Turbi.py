# Missão 3 - Exercícios Turbi

def questao_a():
    valor_original = 3564.98
    valor_pago = 2864.98
    desconto = valor_original - valor_pago
    percentual = (desconto / valor_original) * 100
    return f"a) Desconto de {percentual:.2f}% na primeira mensalidade"

def questao_b():
    valor_mensal = 3564.98
    desconto_percentual = 26  # 26%
    valor_desconto_mensal = valor_mensal * (desconto_percentual / 100)
    return f"b) Desconto mensal de R$ {valor_desconto_mensal:.2f} na assinatura de 6 meses"

def questao_c():
    km_mensal = 15000
    meses = 6
    total_km = km_mensal * meses
    return f"c) Total de km disponíveis: {total_km} km"

# Executar e exibir os resultados
print(questao_a())
print(questao_b())
print(questao_c())