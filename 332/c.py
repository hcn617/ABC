N, M = map(int, input().split())
S = input()

ans = 0  # 購入したロゴTシャツの数
muji, logo = M, 0

for s in S:
    match s:
        case '0':
            muji = M
            logo = ans
        case '1':
            if muji > 0:
                muji -= 1
            elif logo > 0:
                logo -= 1
            else:
                ans += 1
        case '2':
            if logo > 0:
                logo -= 1
            else:
                ans += 1
print(ans)
