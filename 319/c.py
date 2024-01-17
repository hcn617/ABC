from itertools import permutations

c = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
all_cnt = 0
for perm in permutations(range(9), 9):
    all_cnt += 1
    is_ok = True
    for i in range(3):
        P = []
        for j in range(3):
            P.append((perm[i * 3 + j], c[i][j]))
        P.sort()
        if P[0][1] == P[1][1]:
            is_ok = False

    for j in range(3):
        P = []
        for i in range(3):
            P.append((perm[i * 3 + j], c[i][j]))
        P.sort()
        if P[0][1] == P[1][1]:
            is_ok = False

    P = []
    for v in (0, 4, 8):
        i, j = divmod(v, 3)
        P.append((perm[i * 3 + j], c[i][j]))
    P.sort()
    if P[0][1] == P[1][1]:
        is_ok = False

    P = []
    for v in (2, 4, 6):
        i, j = divmod(v, 3)
        P.append((perm[i * 3 + j], c[i][j]))
    P.sort()
    if P[0][1] == P[1][1]:
        is_ok = False

    if is_ok:
        cnt += 1

print(cnt / all_cnt)
