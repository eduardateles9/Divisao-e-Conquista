def melhor_de(a, b):
    return a if (-a[0], a[1], a[2]) <= (-b[0], b[1], b[2]) else b


def dc(v, lo, hi):
    if lo == hi:
        return (v[lo], lo, lo)

    mid = (lo + hi) // 2

    esq = dc(v, lo, mid)
    dir = dc(v, mid + 1, hi)

    s = 0
    melhor_l = float("-inf")
    i_best = mid

    for i in range(mid, lo - 1, -1):
        s += v[i]
        if s >= melhor_l:
            melhor_l = s
            i_best = i

    s = 0
    melhor_r = float("-inf")
    j_best = mid + 1

    for j in range(mid + 1, hi + 1):
        s += v[j]
        if s > melhor_r:
            melhor_r = s
            j_best = j

    cruz = (melhor_l + melhor_r, i_best, j_best)

    return melhor_de(melhor_de(esq, dir), cruz)


def divisao_conquista(v):
    if not v:
        raise ValueError("O vetor não pode ser vazio.")

    return dc(v, 0, len(v) - 1)