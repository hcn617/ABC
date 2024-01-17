N, M = map(int, input().split())
A = list(map(int, input().split()))

ans_lst = [9999999999] * N
for a in A:
    ans_lst[a - 1] = 0

for i in range(N - 2, -1, -1):
    ans_lst[i] = min(ans_lst[i], ans_lst[i + 1] + 1)

for ans in ans_lst:
    print(ans)
