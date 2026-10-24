import sys, random
sys.path.insert(0, "src")
from etapa1_bruta import forca_bruta
from etapa1_dec import divisao_conquista

rng = random.Random(1)
for _ in range(20000):
    n = rng.randint(1, 12)
    v = [rng.randint(-5, 5) for _ in range(n)]
    a, b = forca_bruta(v), divisao_conquista(v)
    if a != b:
        print("DIVERGIU:", v, a, b)
        break
else:
    print("20000 vetores aleatórios: as duas versões concordam")