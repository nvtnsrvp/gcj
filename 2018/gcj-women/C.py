def centrists(l, names):
    return map(cv_ans, [
    possible(l, names, [1, 0, 2]) or possible(l, names, [2, 0, 1]),
    possible(l, names, [0, 1, 2]) or possible(l, names, [2, 1, 0]),
    possible(l, names, [0, 2, 1]) or possible(l, names, [1, 2, 0])
    ])

def cv_ans(ans):
    if ans:
        return 'YES'
    return 'NO'

def possible(l, names, ordering):
    search_on1 = True
    search_on2 = True
    requirements = set()
    # print 'Comparing ' + ' '.join([names[k]for k in ordering])
    for i in range(l):
        if search_on1:
            requirement1 = names[ordering[0]][i] + names[ordering[1]][i]
            constraint1 = names[ordering[1]][i] + names[ordering[0]][i]
            # print '  requirement1 = '+requirement1+' constraint1 = '+constraint1+' '+str(requirements)
            if requirement1[0] != requirement1[1]:
                search_on1 = False
                if constraint1 in requirements:
                    # print 'NO'
                    return False
                else:
                    requirements.add(requirement1)
        if search_on2:
            requirement2 = names[ordering[1]][i] + names[ordering[2]][i]
            constraint2 = names[ordering[2]][i] + names[ordering[1]][i]
            # print '  requirement2 = '+requirement2+' constraint2 = '+constraint2+' '+str(requirements)
            if requirement2[0] != requirement2[1]:
                search_on2 = False
                if constraint2 in requirements:
                    # print 'NO'
                    return False
                else:
                    requirements.add(requirement2)
    # print 'YES'
    return True

t = int(raw_input().strip())
for case in range(1, t+1):
    l = int(raw_input().strip())
    names = raw_input().strip().split()
    print "Case #" + str(case) + ": " + ' '.join(centrists(l, names))
