from itertools import permutations


def grid_iterator():
    for perm_a in permutations(range(N)):
        for perm_b in permutations(range(N)):
            for perm_c in permutations(range(N)):
                is_ok = True
                for aj, bj, cj in zip(perm_a, perm_b, perm_c):
                    if len({aj, bj, cj}) != 3:
                        is_ok = False
                if is_ok:
                    grid = [['.'] * N for _ in range(N)]
                    for i, j in enumerate(perm_a):
                        grid[i][j] = 'A'
                    for i, j in enumerate(perm_b):
                        grid[i][j] = 'B'
                    for i, j in enumerate(perm_c):
                        grid[i][j] = 'C'
                    yield grid


def r_check(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                continue
            if grid[i][j] == R[i]:
                break
            return False
    return True


def c_check(grid):
    for j in range(N):
        for i in range(N):
            if grid[i][j] == '.':
                continue
            if grid[i][j] == C[j]:
                break
            return False
    return True


N = int(input())
R = input()
C = input()

for grid in grid_iterator():
    if r_check(grid) and c_check(grid):
        print("Yes")
        for row in grid:
            print(*row, sep='')
        exit()
print("No")
