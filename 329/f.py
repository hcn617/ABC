N, Q = map(int, input().split())
C = list(map(int, input().split()))

se = [{c} for i, c in enumerate(C)]

for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    if len(se[a]) < len(se[b]):
        se[b] |= se[a]
        se[a] = set()
    else:
        se[a] |= se[b]
        se[a], se[b] = se[b], set()
    print(len(se[b]))
