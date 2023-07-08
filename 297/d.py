A, B = map(int, input().split())

ans = 0
while A != B:
    if A > B:
        A, B = B, A
    cnt, nb = divmod(B, A)
    ans += cnt
    B = nb
    if nb == 0:
        ans -= 1
        break
print(ans)
