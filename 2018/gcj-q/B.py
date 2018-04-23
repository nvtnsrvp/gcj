def trouble_sort(N, V):
    v1, v2 = V[::2], V[1::2]
    v1.sort()
    v2.sort()
    for i in range(len(v1)-1):
        if v1[i] > v2[i]:
            return 2*i
        elif v2[i] > v1[i+1]:
            return 2*i+1
    if len(v1) == len(v2) and v1[-1] > v2[-1]:
        return len(V)-2
    return 'OK'

t = int(raw_input().strip())
for case in range(1, t+1):
    N = int(raw_input().strip())
    V = map(int, raw_input().strip().split())
    print "Case #" + str(case) + ": " + str(trouble_sort(N, V))
