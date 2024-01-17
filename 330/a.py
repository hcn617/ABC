N, L = map(int, input().split())
A = list(map(int, input().split()))

ans = len([a for a in A if a>=L])
print(ans)