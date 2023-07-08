N, K = map(int, input().split())
A = []
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append((a, b))
    cnt += b
A.sort()

if cnt <= K:
    print(1)
    exit()

for i in range(N):
    a, b = A[i]
    cnt -= b
    if cnt <= K:
        print(a + 1)
        exit()
