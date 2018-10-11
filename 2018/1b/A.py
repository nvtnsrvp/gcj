import math

def max_rounding(N, L, C):
    remaining = N - sum(C)
    if remaining == 0:
        return cal_perc(N, C)
    min_perc = 1.0/N*100
    third = min_perc % 1
    if third == 0:
        return 100
    if third > 0.5:
        min_incr = 1
        reason = "third > 0.5"
    else:
        min_incr = int(math.ceil(5.0/(third*10)))
        reason = "third < 0.5"
    g = gcd(100, N)
    min_full = N / g
    # print "remaining="+str(remaining)+" min_incr="+str(min_incr)+"/"+str(N)+" gcd="+str(g)+" min_full="+str(min_full)+' reason('+reason+')'
    pairs = []
    for i in range(L):
        perc = (C[i]*100.0)/N
        dperc = perc - int(perc)
        # print "considering "+str(C[i])+" dperc="+str(dperc)
        if dperc == 0 or dperc >= 0.5:
            pairs.append((0, C[i]))
            continue
        else:
            pairs.append((min_incr - (C[i]%min_full), C[i]))
    pairs.sort()
    # print pairs
    total = 0
    for r, c in pairs:
        if r and remaining - r >= 0:
            remaining -= r
            total += round(100.0*(c+r)/N)
            # print "  1. adding "+str(round(100.0*(c+r)/N))
        else:
            total += round(100.0*c/N)
            # print "  2. adding "+str(round(100.0*c/N))
    # print "  3. adding "+str(math.floor(remaining / min_incr) * round(100.0*min_incr/N))
    total += math.floor(remaining / min_incr) * round(100.0*min_incr/N)
    remaining -= math.floor(remaining / min_incr) * min_incr
    # print "  4. adding "+str(round(100.0*remaining/N))
    total += round(100.0*remaining/N)
    return int(total)

def cal_perc(N, C):
    return int(sum([round(100.0*c/N) for c in C]))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


t = int(raw_input().strip())
for case in range(1, t+1):
    N, L = map(int, raw_input().split())
    C = map(int, raw_input().split())
    print "Case #" + str(case) + ": " + str(max_rounding(N, L, C))
