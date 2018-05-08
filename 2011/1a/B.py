# https://codejam.withgoogle.com/codejam/contest/1145485/dashboard#s=p1
# Problem B. The Killer Word

# Case #1: pajamas caravan
# Case #2: garlic

# Attempt 1:

def killer_words(D, L):
    normalized_d = dict((d, set(d)) for d in D)
    letters = set().union(*normalized_d)
    kw = [killer_word(normalized_d, l, letters) for l in L]
    return ""
    # return ' '.join([killer_word(D, l) for l in L])

def killer_word(normalized_d, l, letters):
    weight = enumerate_guess(l, letters)
    kw = None
    max_weight = 0
    for word, norm_word in normalized_d.iteritems():
        tw = total_weight(weight, norm_word)
        print word, norm_word, tw
        if tw > max_weight:
            max_weight = tw
            kw = word
    return kw

def total_weight(weight, word):
    total = 0
    for c in word:
        total += weight[c]
    return total

def enumerate_guess(l, letters):
    w = 0
    weight = {}
    for c in l:
        if c in letters:
            weight[c] = w
            w += 1
    print l, ' '.join([c + str(weight[c]) for c in l if c in letters])
    return weight

def uniq(word):
    return set(word)

# Attempt 2:

def create_char_mapping(word):
    char_mapping = {}
    for i in range(len(word)):
        if word[i] not in char_mapping:
            char_mapping[word[i]] = []
        char_mapping[word[i]].append(i)
    return char_mapping

def create_mapping(D):
    candidates = {}
    mapping = {}
    for word in D:
        if len(word) not in candidates:
            candidates[len(word)] = set()
            mapping[len(word)] = {}
        candidates[len(word)].add(word)
        char_mapping = create_char_mapping(word)
        for c, positions in char_mapping.iteritems():
            positions = tuple(pos)
            if c not in mapping[len(word)]:
                mapping[len(word)][c] = {}
            if positions not in mapping[len(word)][c][positions]:
                mapping[len(word)][c][positions] = []
            mapping[len(word)][c][positions].append(word)
    return candidates, mapping

def order_guesses(l, mapping):
    ordering = dict((length, '') for length in mapping)
    for length in mapping:
        for c in l:
            if c in ordering[length]:
                ordering[length] += c
    return ordering

def killer_words(D, L):
    candidates, mapping = create_mapping(D)
    for l in L:
        ordering = order_guesses(l, mapping)
        kw = None
        max_score = 0
        for word in D:
            s = score(word, candidates[len(word)], mapping[len(word)], ordering[len(word)])

# Attempt 3: Trees!

def words_by_length(D):
    wl = {}
    for word in D:
        if len(word) not in wl:
            wl[len(D)] = []
        wl[len(D)].append(word)
    return wl

def killer_tree(D, l):
    wl = words_by_length(D)
    kw = None
    max_score = 0
    for (length, words) in wl.iteritems():
        t = build_tree(words, l)
        word, score = traverse(t)
        if score > max_score:
            max_score = score
            kw = word
    return kw

def create_edges(words):
    edges = {}
    for word in words:
        char_mapping = create_char_mapping(word)
        for c, positions in char_mapping.iteritems():
            positions = tuple(positions)
            if c not in edges:
                edges[c] = {}
            if positions not in edges[c]:
                edges[c][positions] = set()
            edges[c][positions].add(word)
    return edges

def build_tree(words, l):
    edges = create_edges(words)
    agenda = [Node(words, l, 0)]
    while agenda:
        pass

class Node:
    def __init__(self, candidates, l, i, edges, level=0):
        self.candidates = candidates
        self.l = l
        self.i = i
        self.level = level
        self.edges = edges
        if len(self.condidate) <= 1:
            self.children = None
        else:
            self.children = self.init_children()

    def init_children(self):
        self.children = []
        for j in range(self.i, len(self.l)):
            if self.l[j] not in self.edges:
                continue
            self.i = j
            for positions, words in self.edges[l[j]]:
                new_candidates = self.condidate.intersect(words)
                self.children.append(Node(new_candidates, l, j+1, edges, self.level+1))


t = int(raw_input().strip())
for case in range(1, t+1):
    N, M = map(int, raw_input().split())
    D = [raw_input().strip() for i in range(N)]
    L = [raw_input().strip() for i in range(M)]
    print "Case #" + str(case) + ": " + str(killer_words(D, L))
