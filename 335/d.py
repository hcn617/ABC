V = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
Grid = [[0] * N for _ in range(N)]
Grid[N // 2][N // 2] = 'T'

x = 1
for i in range(N // 2):
    l = (N - 1) - i * 2
    ni, nj = i, i
    for vi, vj in V:
        for _ in range(l):
            Grid[ni][nj] = x
            ni += vi
            nj += vj
            x += 1
for row in Grid:
    print(*row)
