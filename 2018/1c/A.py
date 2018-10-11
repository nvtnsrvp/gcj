def new_word(N, L, words):
    swords = set(words)
    letters = [0]*L
    for i in range(L):
        letters[i] = list(set(words[j][i]for j in range(N)))
    for p in permute(letters, 0):
        if p not in swords:
            return p
    return '-'

def permute(letters, j):
    if len(letters) == j:
        return []
    words = permute(letters, j+1)
    # print "j = "+str(j) + " previous = "+str(words)
    # print len(words)
    if not words:
        return letters[j]
    p = []
    for letter in letters[j]:
        for w in words:
            p.append(letter + w)
    return p

t = int(raw_input().strip())
for case in range(1, t+1):
    N, L = map(int, raw_input().split())
    words = [raw_input().strip() for i in range(N)]
    print "Case #" + str(case) + ": " + str(new_word(N, L, words))
