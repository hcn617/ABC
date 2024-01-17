M = int(input())
D = list(map(int, input().split()))
lst = []
for i in range(M):
    for j in range(D[i]):
        lst.append((i + 1, j + 1))
a, b = lst[sum(D) // 2]
print(a, b)
