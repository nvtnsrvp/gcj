import math
def min_hacks(D, P):
    """
    integer D: the maximum total damage our shield can withstand,
    string P: the robot's program.
    """
    # print P
    total, s_positions = strength(P)
    if len(s_positions) > D:
        return 'IMPOSSIBLE'
    if total <= D:
        return 0
    num_hacks = 0
    s_positions.reverse()
    # print total, s_positions
    for j in range(len(s_positions)):
        s = s_positions[j]
        if s == j:
            continue
        value = 2**(s-j) - 1
        # print "s"+str(j)+" at "+str(s)+" value: "+str(value)+" remaining: "+str(total-D)
        if total - D >= value:
            # print "  total("+str(total)+") - D("+str(D)+") > value("+str(value)+")"
            num_hacks += (s-j)
            total = total - value
        else:
            # print "  total("+str(total)+") - D("+str(D)+") < value("+str(value)+")"
            num_hacks += int(math.ceil(math.log((total-D),2.0)))
            total = D
        # print "  total: "+str(total)+" num_hacks: "+str(num_hacks)
        if total <= D:
            return num_hacks
    return 'IMPOSSIBLE'

def strength(P):
    s_positions = []
    total = 0
    for i in range(len(P)-1, -1, -1):
        if P[i] == 'C':
            total *=2
        elif P[i] == 'S':
            total += 1
            s_positions.append(i)
    return total, s_positions

t = int(raw_input().strip())
for case in range(1, t+1):
    D, P = raw_input().split()
    print "Case #" + str(case) + ": " + str(min_hacks(int(D), P))
