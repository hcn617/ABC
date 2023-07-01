N = int(input())
A = list(map(int,input().split()))

ans = []
for i in range(N):
    value = sum(A[7 * i:7 * (i + 1)])
    ans.append(value)

print(*ans)