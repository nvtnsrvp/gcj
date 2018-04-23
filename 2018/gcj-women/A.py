def bun_error(K, D):
    int_d = [int(di) for di in D.split()]
    int_d.sort()
    return sum([(int_d[i]-int(i/2))**2 for i in range(int(K))])

t = int(raw_input().strip())
for case in range(1, t+1):
    K = int(raw_input().strip())
    D = raw_input().strip()
    print "Case #" + str(case) + ": " + str(bun_error(K, D))
