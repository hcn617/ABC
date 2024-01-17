N = int(input())
A = set(map(int, input().split()))
A.discard(max(A))
print(max(A))
