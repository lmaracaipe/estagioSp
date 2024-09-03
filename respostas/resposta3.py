import json

# Exemplo de dados de faturamento
dados_json = '''
{
    "faturamento_diario": [1000, 2000, 0, 500, 0, 3000, 700]
}
'''

dados = json.loads(dados_json)
faturamento = [valor for valor in dados['faturamento_diario'] if valor > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento}")
print(f"Maior valor de faturamento: R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
