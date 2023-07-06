N, K = map(int, input().split())
A = [int(a) - 1 for a in input().split()]

# nex[i][j]: 町iから1<<j回だけテレポートした先の町idx
nex = [[-1] * 63 for _ in range(N)]
for i in range(N):
    nex[i][0] = A[i]

for j in range(1, 63):
    for i in range(N):
        mid = nex[i][j - 1]
        nex[i][j] = nex[mid][j - 1]
town = 0
for j in range(63):
    if K & 1:
        town = nex[town][j]
    K >>= 1
print(town + 1)
