N, M = map(int, input().split())

P = []
F = []
for _ in range(N):
    p, c, *f = map(int, input().split())
    P.append(p)
    se = set()
    for el in f:
        se.add(el)
    F.append(se)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if P[i] < P[j]:
            continue

        is_ok = True
        for el in F[i]:
            if el not in F[j]:
                is_ok = False
        if not is_ok:
            continue

        if P[i] > P[j]:
            print("Yes")
            exit()

        for el in F[j]:
            if el not in F[i]:
                print("Yes")
                exit()

print("No")
