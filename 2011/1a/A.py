# https://codejam.withgoogle.com/codejam/contest/1145485/dashboard
# Problem A. FreeCell Statistics

def stat(N, Pd, Pg):
    # print "Pg: "+str(Pg)+"/100 Pd:"+str(Pd)+"/100 N("+str(N)+") >= "+str(100/g)
    if Pg == 0:
        if Pd == 0:
            return 'Possible'
        return 'Broken'
    if Pg == 100:
        if Pd == 100:
            return 'Possible'
        return 'Broken'
    g = gcd(100, Pd)
    # print "Pg: "+str(Pg)+"/100 Pd:"+str(Pd)+"/100 GCD:"+str(g)+" => Pd:"+str(Pd/g)+"/"+str(100/g)+" N("+str(N)+") >= "+str(100/g)
    if N >= 100 / g:
        return 'Possible'
    return 'Broken'

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

t = int(raw_input().strip())
for case in range(1, t+1):
    N, Pd, Pg = map(int, raw_input().split())
    print "Case #" + str(case) + ": " + str(stat(N, Pd, Pg))
