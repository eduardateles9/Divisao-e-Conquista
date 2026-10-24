import csv
from collections import defaultdict
import matplotlib.pyplot as plt

dados = defaultdict(list)
with open("dados/etapa1_medicoes.csv") as f:
    for r in csv.DictReader(f):
        dados[(r["algoritmo"], int(r["n"]))].append(float(r["tempo_ms"]))

plt.figure()
for alg, rotulo in (("bruta", "Força bruta O(n²)"), ("dc", "Divisão e conquista O(n log n)")):
    ns = sorted(n for (a, n) in dados if a == alg)
    medias = [sum(dados[(alg, n)]) / len(dados[(alg, n)]) for n in ns]
    plt.plot(ns, medias, marker="o", label=rotulo)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("tempo médio (ms)")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.savefig("relatorio/etapa1_grafico.png", dpi=150)