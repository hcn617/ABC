se = set()
for i in range(100):
    for j in range(100):
        se.add((2 ** i) * (3 ** j))

N = int(input())
if N in se:
    print("Yes")
else:
    print("No")
