import csv, random, time
from etapa1_bruta import forca_bruta
from etapa1_dec import divisao_conquista

TAMANHOS = [10, 20, 50, 100, 200, 400, 800, 1600, 3200, 6400]
EXECUCOES = 5
rng = random.Random(42)

with open("dados/etapa1_medicoes.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["etapa", "algoritmo", "n", "execucao", "tempo_ms"])
    for n in TAMANHOS:
        for e in range(1, EXECUCOES + 1):
            v = [rng.randint(-100, 100) for _ in range(n)]
            for nome, alg in (("bruta", forca_bruta), ("dc", divisao_conquista)):
                t0 = time.perf_counter()
                alg(v)
                t1 = time.perf_counter()
                w.writerow([1, nome, n, e, (t1 - t0) * 1000])
        print("n =", n, "ok")