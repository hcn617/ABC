N, M = map(int, input().split())
Black = [list(map(int, input().split())) for _ in range(M)]
Black.sort()

dic = dict()
for bi, bj in Black:
    if bi not in dic:
        idx = len(dic)
        dic[bi] = idx

for j in range(M):
    Black[j][0] = dic[Black[j][0]]

G = [set() for _ in range(len(dic))]
for bi, bj in Black:
    G[bi].add(bj)

vs = {N}
for gr in G:
    discard_set = set()
    add_set = set()
    for v in gr:
        if v in vs:
            discard_set.add(v)
        if v + 1 in vs:
            add_set.add(v)
        if v - 1 in vs:
            add_set.add(v)
    for v in discard_set:
        vs.discard(v)
    for v in add_set:
        vs.add(v)
    # print(vs)
print(len(vs))
