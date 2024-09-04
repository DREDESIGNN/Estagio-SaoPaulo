# Questão 04 - Estagio - São Paulo
# Valores de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento.values())

# Calcula e exibe o percentual de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f'{estado}: {percentual:.2f}%')

# Exibe o faturamento total
print(f'\nFaturamento Total: R${faturamento_total:.2f}')
