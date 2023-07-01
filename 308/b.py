N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

dic = dict()
for i in range(M):
    dic[D[i]] = P[i + 1]

ans = 0
for c in C:
    if c not in dic:
        ans += P[0]
    else:
        ans += dic[c]
print(ans)
