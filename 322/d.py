# 時計回りに90度だけまわしたものを返す
def rotate90(grid):
    return list(zip(*reversed(grid)))

# def rotate90(grid):
#     ret = [['.'] * 4 for _ in range(4)]
#     for i in range(4):
#         for j in range(4):
#             ret[i][j] = grid[j][3 - i]
#     return ret


# 上下に平行移動できるものをすべて格納したリストを返す。
def pattern_row(grid):
    ret = [grid]
    for i in range(3):
        if '#' in grid[i]:
            break
        nex = [['.'] * 4 for _ in range(4)]
        for ii in range(i + 1, 4):
            for jj in range(4):
                nex[ii - i - 1][jj] = grid[ii][jj]
        ret.append(nex)
    for i in range(3, 0, -1):
        if '#' in grid[i]:
            break
        nex = [['.'] * 4 for _ in range(4)]
        for ii in range(i):
            for jj in range(4):
                nex[ii + (4 - i)][jj] = grid[ii][jj]
        ret.append(nex)
    return ret


# 左右に平行移動できるものをすべて格納したリストを返す。
def pattern_col(grid):
    def all_dot(g, nj):
        for i in range(4):
            if g[i][nj] == '#': return False
        return True

    ret = [grid]
    for j in range(3):
        if not all_dot(grid, j):
            break
        nex = [['.'] * 4 for _ in range(4)]
        for ii in range(4):
            for jj in range(j + 1, 4):
                nex[ii][jj - j - 1] = grid[ii][jj]
        ret.append(nex)
    for j in range(3, 0, -1):
        if not all_dot(grid, j):
            break
        nex = [['.'] * 4 for _ in range(4)]
        for ii in range(4):
            for jj in range(j):
                nex[ii][jj + (4 - j)] = grid[ii][jj]
        ret.append(nex)
    return ret


# 上下左右に平衡移動してできるものすべてを格納したリストを返す。
def pattern_all(grid):
    ret = []
    for p1 in pattern_row(grid):
        for p2 in pattern_col(p1):
            ret.append(p2)
    return ret


# 回転・上下左右の平行移動をしてできるものすべてを格納したリストを返す。
def pattern_rotate_all(grid1):
    grid2 = rotate90(grid1)
    grid3 = rotate90(grid2)
    grid4 = rotate90(grid3)
    ret = []
    for grid_r in [grid1, grid2, grid3, grid4]:
        for grid in pattern_all(grid_r):
            ret.append(grid)
    return ret


# この3つで、衝突なしで全部のマスを埋められたらTrue
def is_ok(p1, p2, p3):
    grid = [[False] * 4 for _ in range(4)]
    for p in [p1, p2, p3]:
        for i in range(4):
            for j in range(4):
                if p[i][j] == '#':
                    if not grid[i][j]:
                        grid[i][j] = True
                    else:
                        return False
    for i in range(4):
        for j in range(4):
            if not grid[i][j]:
                return False
    return True


Ps = []

for _ in range(3):
    P = [list(input()) for _ in range(4)]
    Ps.append(P)

A = []
for grid in Ps:
    A.append(pattern_rotate_all(grid))

for p1 in A[0]:
    for p2 in A[1]:
        for p3 in A[2]:
            if is_ok(p1, p2, p3):
                print("Yes")
                exit()
print("No")
