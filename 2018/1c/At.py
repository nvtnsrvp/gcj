# Attempt 1:
# def new_word(N, L, words):
#     swords = set(words)
#     letters = [0]*L
#     for i in range(L):
#         letters[i] = list(set(words[j][i]for j in range(N)))
#     for p in permute(letters, 0):
#         if p not in swords:
#             return p
#     return '-'

# def permute(letters, j):
#     if len(letters) == j:
#         return []
#     words = permute(letters, j+1)
#     # print "j = "+str(j) + " previous = "+str(words)
#     # print len(words)
#     if not words:
#         return letters[j]
#     p = []
#     for letter in letters[j]:
#         for w in words:
#             p.append(letter + w)
#     return p

# Attempt 2:
def old_stat(swords):


def new_word(N, L, words):
    swords = set(words)
    letters = [0]*N
    for i in range(L):
        letters[i] = set(words[j][i] for j in range(N))

    for

    num_letter = [{} for i in range(10)]
    for i in range(L):
        for j in range(N):
            print words[i][j]
            if words[i][j] not in num_letter[i]:
                num_letter[i][words[j][i]] = 0
            #print "j = "+str(j)+" previous " + str(words[j])
            num_letter[i][words[j][i]] += 1

    num_permu = 1
    for i in range(L):
        num_permu *= length(letters[i])

    list_permu = [num_permu] * L
    for i in range(L):
        list_permu[i] /= length(letters[i])

    for i in range(L):
        for letters in letters[i]:
            if num_Letter[i][letters] < list_permu[i]:
                output[i] = letters
                break
        if output[i] == '0':
            return '-'
    return output

t = int(raw_input().strip())
for case in range(1, t+1):
    N, L = map(int, raw_input().split())
    words = [raw_input().strip() for i in range(N)]
    print "Case #" + str(case) + ": " + str(new_word(N, L, words))


t = int(raw_input().strip())
for case in range(1, t+1):
    N, L = map(int, raw_input().split())
    words = [raw_input().strip() for i in range(N)]
    # new_word(N, L, words)
    print "Case #" + str(case) + ": " + str(new_word(N, L, words))
