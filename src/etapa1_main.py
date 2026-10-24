import sys
from etapa1_bruta import forca_bruta
from etapa1_dec import divisao_conquista

def ler(arquivo):
    texto = open(arquivo).read() if arquivo else sys.stdin.read()
    tokens = texto.split()
    n = int(tokens[0])
    return [int(x) for x in tokens[1:1 + n]]

if __name__ == "__main__":
    algoritmo = sys.argv[1]                       # "bruta" ou "dc"
    arquivo = sys.argv[2] if len(sys.argv) > 2 else None
    v = ler(arquivo)
    f = forca_bruta if algoritmo == "bruta" else divisao_conquista
    soma, inicio, fim = f(v)
    print(soma, inicio, fim)