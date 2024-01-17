N, X = map(int, input().split())
S = list(map(int, input().split()))

ans = sum(s for s in S if s <= X)
print(ans)
