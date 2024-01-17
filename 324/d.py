from collections import Counter

N = int(input())
S = input()

max_num = 10 ** N
C = Counter(S)
sq = 0
ans = 0

while (num := sq * sq) < max_num:
    str_num = str(num).zfill(N)
    if Counter(str_num) == C:
        ans += 1
    sq += 1

print(ans)
