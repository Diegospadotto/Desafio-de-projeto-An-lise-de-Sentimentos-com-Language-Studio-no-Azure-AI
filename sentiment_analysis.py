import requests

# Chave de assinatura e endpoint
subscription_key = 'sua-chave-de-assinatura'
endpoint = 'https://sua-regiao.cognitiveservices.azure.com/'

# URL para a análise de sentimentos
sentiment_url = endpoint + "text/analytics/v3.1/sentiment"

headers = {"Ocp-Apim-Subscription-Key": subscription_key}

# Função para análise de sentimentos
def analisar_sentimento(texto):
    documents = {
        "documents": [
            {"id": "1", "language": "pt", "text": texto}
        ]
    }

    response = requests.post(sentiment_url, headers=headers, json=documents)
    if response.status_code == 200:
        sentiments = response.json()
        for document in sentiments["documents"]:
            print(f"Texto: {document['id']}")
            print(f"Sentimento: {document['sentiment']}")
            print(f"Confiança: {document['confidenceScores']}")
    else:
        print(f"Erro na requisição: {response.status_code}")

if __name__ == '__main__':
    # Teste com textos de exemplo
    with open('data/sample_texts.txt', 'r', encoding='utf-8') as file:
        textos = file.readlines()

    for texto in textos:
        print(f"Analisando: {texto.strip()}")
        analisar_sentimento(texto.strip())
