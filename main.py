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


if __name__ == '__main__':
    frase1 = "Hello everyone, nice to meet you all"
    pontuacao_de_sentimentos(frase1)

    frase2 = "I'm kinda sick today"
    pontuacao_de_sentimentos(frase2)

    frase3 = "It was a common reaction"
    pontuacao_de_sentimentos(frase3)
