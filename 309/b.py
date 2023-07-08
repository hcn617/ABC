N = int(input())
A = [input() for _ in range(N)]

B = []
for a in A:
    B.append(list(a))
for j in range(N - 1):
    B[0][j + 1] = A[0][j]
    B[-1][j] = A[-1][j + 1]
for i in range(N - 1):
    B[i + 1][-1] = A[i][-1]
    B[i][0] = A[i + 1][0]
for b in B:
    print(*b, sep="")
