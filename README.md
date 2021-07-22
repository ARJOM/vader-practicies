# Estudo Vader

Esse repositório é destinado ao estudo da biblioteca Vader, focada em seu uso para processamento de emoções em textos.

Exemplo de saída da função pontuacao_de_sentimentos
```
--------------------------------------------------
Hello everyone, nice to meet you all
Dicionário de sentimentos é:  {'neg': 0.0, 'neu': 0.682, 'pos': 0.318, 'compound': 0.4215}
frase foi classificada como  0.0 % negativa
frase foi classificada como  68.2 % neutra
frase foi classificada como  31.8 % positiva
Frase avaliada no geral como Positiva
--------------------------------------------------
I'm kinda sick today
Dicionário de sentimentos é:  {'neg': 0.501, 'neu': 0.499, 'pos': 0.0, 'compound': -0.4601}
frase foi classificada como  50.1 % negativa
frase foi classificada como  49.9 % neutra
frase foi classificada como  0.0 % positiva
Frase avaliada no geral como Negativa
--------------------------------------------------
It was a common reaction
Dicionário de sentimentos é:  {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
frase foi classificada como  0.0 % negativa
frase foi classificada como  100.0 % neutra
frase foi classificada como  0.0 % positiva
Frase avaliada no geral como Neutra

```

Exemplo de saída do código atual
```
39.748640030013135% das amostras foram classificadas, corretamente, como negativas
82.98630650909773% das amostras foram classificadas, corretamente, como positivas
```