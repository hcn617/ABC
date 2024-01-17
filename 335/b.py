from itertools import product

N = int(input())
for pro in product(range(N + 1), repeat=3):
    if sum(pro) <= N:
        print(*pro)
