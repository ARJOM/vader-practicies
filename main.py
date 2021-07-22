from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def pontuacao_de_sentimentos(frase: str):
    analisador = SentimentIntensityAnalyzer()
    dicionario_de_sentimentos: dict = analisador.polarity_scores(frase)

    print(50*"-")
    print(frase)
    print("Dicionário de sentimentos é: ", dicionario_de_sentimentos)
    print("frase foi classificada como ", dicionario_de_sentimentos['neg'] * 100, "% negativa")
    print("frase foi classificada como ", dicionario_de_sentimentos['neu'] * 100, "% neutra")
    print("frase foi classificada como ", dicionario_de_sentimentos['pos'] * 100, "% positiva")

    print("Frase avaliada no geral como", end=" ")

    if dicionario_de_sentimentos['compound'] >= 0.05:
        print("Positiva")
    elif dicionario_de_sentimentos['compound'] <= -0.05:
        print("Negativa")
    else:
        print("Neutra")


def analise_de_sentimentos(frase:str, opcao:str):
    analisador = SentimentIntensityAnalyzer()
    dicionario_de_sentimentos: dict = analisador.polarity_scores(frase)

    if dicionario_de_sentimentos['neg'] > dicionario_de_sentimentos['pos']:
        resultado = 'negativa'
    else:
        resultado = 'positiva'

    if resultado == opcao:
        return 1
    return 0


if __name__ == '__main__':
    with open("negativo.txt", "r") as arquivo:
        linhas = arquivo.read().split('\n')
        total = len(linhas)
        count_neg = 0
        for linha in linhas:
            count_neg += analise_de_sentimentos(linha, 'negativa')
        print(f"{(count_neg/total)*100}% das amostras foram classificadas, corretamente, como negativas")

    with open("positivo.txt", "r") as arquivo:
        linhas = arquivo.read().split('\n')
        total = len(linhas)
        count_pos = 0
        for linha in linhas:
            count_pos += analise_de_sentimentos(linha, 'positiva')
        print(f"{(count_pos/total)*100}% das amostras foram classificadas, corretamente, como positivas")
