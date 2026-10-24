def forca_bruta(v):
    n = len(v)
    melhor = (v[0], 0, 0)          # (soma, inicio, fim)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += v[j]              # acumula, não recalcula do zero
            if s > melhor[0]:      # > estrito: mantém o primeiro empate
                melhor = (s, i, j)
    return melhor