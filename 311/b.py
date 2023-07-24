N, D = map(int, input().split())

T = ['o'] * D  # T[i]: i日目が全員ヒマなら'o', そうじゃないなら'x'
for _ in range(N):
    S = input()
    for i in range(D):
        if S[i] == 'x':
            T[i] = 'x'

prev = 0
ans = 0
for t in T:
    if t == 'o':
        prev += 1
        ans = max(ans, prev)
    else:
        prev = 0

print(ans)
