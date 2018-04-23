memo={}

def bit_party(R, B, C, cashiers):
    return bits_min_time(R, B, C-1, cashiers)

def bits_min_time(r, b, c, cashiers):
    M, S, P = cashiers[c]
    min_t = float("inf")
    for m in range(min(M, b)):
        if m == 0:
            prer = r
        else:
            prer = r - 1
        preb = b - m
        prec = c - 1
        if (prer, preb, prec) in memo:
            pret = memo[(prer, preb, prec)]
        else:
            pret = bits_min_time(prer, preb, prec, cashiers)
        t = (m*S + P)
        min_t = min(min_t, max(t, pret))
    memo[(prer, preb, prec)] = min_t
    return min_t

t = int(raw_input().strip())
for case in range(1, t+1):
    R, B, C = map(int, raw_input().split())
    cashiers = [map(int, raw_input().split()) for i in range(C)]
    print "Case #" + str(case) + ": " + str(bit_party(R, B, C, cashiers))
