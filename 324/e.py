from bisect import bisect_left

# 文字列Bの先頭何文字が文字列Aの部分文字列になっているか
def f(A, B):
    j = 0
    for i, a in enumerate(A):
        if a == B[j]:
            j += 1
            if j == len(B):
                break
    return j


N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

rev_T = T[::-1]
left = [0] * N
right = [0] * N
for i in range(N):
    left[i] = f(S[i], T)
    right[i] = f(S[i][::-1], rev_T)

right.sort()
ans = 0
for le in left:
    ans += N - bisect_left(right, len(T) - le)
print(ans)
