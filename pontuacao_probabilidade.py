import scipy.stats as sp
import statistics as sts
import matplotlib.pyplot as plt

# Pontuações anteriores desde 2006 (ano em que passou a possuir 20 times)
pc = [78,77,75,67,71,71,77,76,80,81,80,72,80,90,71,84,81]

def graficoprob():
    probs = []
    kvetor = []
    for k in range(0,101):
        prob = probporpont(k)
        probs.append(prob)
        kvetor.append(k)

    plt.plot(kvetor,probs)
    plt.xlabel("Pontuação")
    plt.ylabel("Probabilidade")
    plt.show()

def probporpont(p):
    z = (p-sts.mean(pc))/sts.stdev(pc)
    prob = sp.norm.cdf(z)
    return prob

r = int(input("Digite uma pontuação: "))
print(f"A probabilidade para essa pontuação é: {round(probporpont(r)*100,2)}%")

graficoprob()