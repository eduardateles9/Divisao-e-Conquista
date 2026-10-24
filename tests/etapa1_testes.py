import sys
sys.path.insert(0, "src")
from etapa1_bruta import forca_bruta
from etapa1_dec import divisao_conquista

ok = True
with open("tests/etapa1_casos.txt", encoding="utf-8") as f:
    for linha in f:
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        nome, entrada, saida = [p.strip() for p in linha.split("|")]
        v = [int(x) for x in entrada.split()[1:]]
        esperado = tuple(int(x) for x in saida.split())
        for nome_alg, alg in (("bruta", forca_bruta), ("dc", divisao_conquista)):
            obtido = alg(v)
            if obtido != esperado:
                ok = False
                print(f"FALHOU [{nome}] {nome_alg}: esperado {esperado}, obtido {obtido}")
print("Todos os casos passaram" if ok else "Há falhas")