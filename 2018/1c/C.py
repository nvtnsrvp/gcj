def ant_stack(N, W):
    K = [[0 for w in range(sum(W)+1)] for i in range(N+1)]
    capacity = [ 6*w for w in W ]
    for i in range(N+1):
        for w in range(sum(W)+1):
            # print "considering i="+str(i)+" w="+str(w)
            if i == 0 or w == 0:
               K[i][w] = 0
            elif w >= W[i-1] and w <= capacity[i-1]:
                K[i][w] = max(1 + K[i-1][w-W[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    # for
    #     elif w >= W[i] and w <= capacity[i]:
    #         K[i][w] = max(1 + K[i-1][w-W[i]],  K[i-1][w])
    #     else:
    #         K[i][w] = K[i-1][w]
    return max(K[N-1])

t = int(raw_input().strip())
for case in range(1, t+1):
    N = int(raw_input())
    W = map(int, raw_input().split())
    print "Case #" + str(case) + ": " + str(ant_stack(N, W))
