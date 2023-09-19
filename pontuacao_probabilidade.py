import scipy.stats as sp
import statistics as sts
import matplotlib.pyplot as plt

# Pontuações anteriores desde 2006 (ano em que passou a possuir 20 times)
pc = [78, 77, 75, 67, 71, 71, 77, 76, 80, 81, 80, 72, 80, 90, 71, 84, 81]

def testar_normalidade(dados):
    _, p_valor = sp.shapiro(dados)
    return p_valor > 0.05

def calcular_probabilidade(pontuacao, dados):
    media = sts.mean(dados)
    desvio_padrao = sts.stdev(dados)
    z_score = (pontuacao - media) / desvio_padrao
    probabilidade = sp.norm.cdf(z_score)
    return probabilidade * 100

def criar_grafico_probabilidade(dados):
    probabilidades = []
    pontuacoes = list(range(0, 101))
    for pontuacao in pontuacoes:
        prob = calcular_probabilidade(pontuacao, dados)
        probabilidades.append(prob)
        if prob == 100:
            break

    plt.plot(pontuacoes, probabilidades)
    plt.xlabel("Pontuação")
    plt.ylabel("Probabilidade")
    plt.show()

if testar_normalidade(pc):
    pontuacao = int(input("Digite uma pontuação: "))
    probabilidade = calcular_probabilidade(pontuacao, pc)
    print(f"A probabilidade para essa pontuação é: {round(probabilidade, 2)}%")
    criar_grafico_probabilidade(pc)
else:
    print("O teste de normalidade não passou. O z-score não é a abordagem adequada para calcular esta probabilidade.")