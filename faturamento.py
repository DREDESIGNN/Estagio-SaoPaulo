# Questão 03 - Estagio - São Paulo
import json

def carregar_dados_json(caminho_arquivo):
    """
    Carrega dados de um arquivo JSON.
    """
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados['faturamento_diario']

def calcular_faturamento(dados):
    """
    Calcula o menor e maior valor de faturamento, além do número de dias com faturamento acima da média.
    """
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    
    if not valores:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_media": 0
        }
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media
    }

def main():
    # Carregar dados do arquivo JSON
    caminho_arquivo = 'faturamento.json'
    dados = carregar_dados_json(caminho_arquivo)
    
    # Calcular valores
    resultado = calcular_faturamento(dados)
    
    # Exibir resultados
    print(f"Menor valor de faturamento: {resultado['menor_valor']}")
    print(f"Maior valor de faturamento: {resultado['maior_valor']}")
    print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_media']}")

if __name__ == "__main__":
    main()
