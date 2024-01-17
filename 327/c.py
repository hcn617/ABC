# 各行に1～9が入っているかチェックする
def row_check():
    for i in range(9):
        se = set()
        for j in range(9):
            se.add(A[i][j])
        if len(se) != 9:
            return False
    return True


# 各列に1～9が入っているかチェックする
def col_check():
    for j in range(9):
        se = set()
        for i in range(9):
            se.add(A[i][j])
        if len(se) != 9:
            return False
    return True


# 各3×3のマスに1～9が入っているかチェックする
def square_check():
    for si in [0, 3, 6]:
        for sj in [0, 3, 6]:
            se = set()
            for di in range(3):
                for dj in range(3):
                    i, j = si + di, sj + dj
                    se.add(A[i][j])
            if len(se) != 9:
                return False
    return True


A = [list(map(int, input().split())) for _ in range(9)]
if row_check() and col_check() and square_check():
    print("Yes")
else:
    print("No")
