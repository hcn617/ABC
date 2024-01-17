N = int(input())

G = [[] for _ in range(N)]
for p in range(1, N + 1):
    S = input()
    win_cnt = S.count('o')
    G[win_cnt].append(p)

for i in range(N - 1, -1, -1):
    for p in G[i]:
        print(p, end=' ')
