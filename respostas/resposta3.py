import json

# Carregar os dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Extrair os valores de faturamento, ignorando dias sem faturamento
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Cálculos solicitados
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

# Contar o número de dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
