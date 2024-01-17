H, W = map(int, input().split())
Grid = [list(input()) for _ in range(H)]

# アルファベットを整数に変換
for i in range(H):
    for j in range(W):
        Grid[i][j] = ord(Grid[i][j]) - ord('a')

# row[i][num]: i行目にある数字numの個数
row = [[0] * 26 for _ in range(H)]
col = [[0] * 26 for _ in range(W)]
# row_color_cnt[i]: i行目にある数字の種類数
row_color_cnt = [0] * H
col_color_cnt = [0] * W

for i in range(H):
    for j in range(W):
        num = Grid[i][j]
        if row[i][num] == 0:
            row_color_cnt[i] += 1
        if col[j][num] == 0:
            col_color_cnt[j] += 1
        row[i][num] += 1
        col[j][num] += 1

# now_H: 削除されていない行の数
now_H, now_W = H, W
# deleted_row[i]: i行目が操作1によって削除されていればTrue
deleted_row = [False] * H
deleted_col = [False] * W

while now_H >= 2 or now_W >= 2:
    now_delete_row = []
    dec_H = 0
    for i in range(H):
        if deleted_row[i]:
            continue
        if row_color_cnt[i] == 1 and now_W >= 2:
            deleted_row[i] = True
            now_delete_row.append(i)
            dec_H += 1
    now_delete_col = []
    dec_W = 0
    for j in range(W):
        if deleted_col[j]:
            continue
        if col_color_cnt[j] == 1 and now_H >= 2:
            deleted_col[j] = True
            now_delete_col.append(j)
            dec_W += 1
    now_H -= dec_H
    now_W -= dec_W

    if len(now_delete_row) == len(now_delete_col) == 0:
        break

    for i in now_delete_row:
        for j in range(W):
            if not deleted_col[j]:
                num = Grid[i][j]
                if num == -1:
                    continue
                col[j][num] -= 1
                Grid[i][j] = -1
                if col[j][num] == 0:
                    col_color_cnt[j] -= 1

    for j in now_delete_col:
        for i in range(H):
            if not deleted_row[i]:
                num = Grid[i][j]
                if num == -1:
                    continue
                row[i][num] -= 1
                Grid[i][j] = -1
                if row[i][num] == 0:
                    row_color_cnt[i] -= 1

print(now_H * now_W)
