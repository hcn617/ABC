S = list(map(int, input().split()))

for el in S:
    if not (100 <= el <= 675 and el % 25 == 0):
        print("No")
        exit()

for i in range(7):
    if S[i] > S[i + 1]:
        print("No")
        exit()

print("Yes")
