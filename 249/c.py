from itertools import product

N, K = map(int, input().split())
C = []
for _ in range(N):
    S = input()
    c = [0] * 26
    for s in S:
        c[ord(s) - ord('a')] += 1
    C.append(c)

ans = 0
for pro in product((0, 1), repeat=N):
    cnt = [0] * 26
    now_ans = 0
    for c, pr in zip(C, pro):
        if not pr: continue
        for i in range(26):
            cnt[i] += c[i]
    for el in cnt:
        if el == K:
            now_ans += 1
    ans = max(ans, now_ans)
print(ans)
