A, B = map(int, input().split())
P = [
    (1, 2),
    (2, 3),
    (4, 5),
    (5, 6),
    (7, 8),
    (8, 9)
]
if (A, B) in P:
    print("Yes")
else:
    print("No")
