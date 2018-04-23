def find_ceo(org):
    capacity = [n*e for n, e in org]
    remaining_req = 0
    for i in range(len(org)-1):
        n, e = org[i]
        if n+remaining_req > capacity[i+1]:
            remaining_req = n+remaining_req - capacity[i+1]
        else:
            remaining_req = 0
    remaining_req = remaining_req + org[-1][0]
    max_level = org[-1][1]
    return max(max_level+1, remaining_req)

t = int(raw_input().strip())
for case in range(1, t+1):
    l = int(raw_input().strip())
    org = [ map(int, raw_input().strip().split()) for level in range(l) ]
    print "Case #" + str(case) + ": " + str(find_ceo(org))
