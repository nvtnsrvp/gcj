import numpy as np

def waffle_choppers(R, C, H, V, waffle):
    nshares = (H+1)*(V+1)
    msum = np.sum(waffle)
    if msum % nshares:
        return "IMPOSSIBLE"
    each = msum / nshares
    hsum, vsum = np.sum(waffle, axis=1), np.sum(waffle, axis=0)
    for i in range(hsum.shape[0]):
        if hsum[i, 0] > (V+1)*each:
            return "IMPOSSIBLE"
    for j in range(vsum.shape[1]):
        if vsum[0, j] > (H+1)*each:
            return "IMPOSSIBLE"
    return "OOPPP"

def bin(c):
    if c == "@":
        return 1
    else:
        return 0

t = int(raw_input().strip())
for case in range(1, t+1):
    R, C, H, V = map(int, raw_input().split())
    waffle = np.matrix([[bin(c) for c in raw_input().strip()] for i in range(R)])
    waffle_choppers(R, C, H, V, waffle)
    print "Case #" + str(case) + ": " + str(waffle_choppers(R, C, H, V, waffle))
