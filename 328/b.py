def is_ok(A, B):
    str_month = str(A)
    str_day = str(B)
    str_month_day = str_month + str_day
    se = set()
    for element in str_month_day:
        se.add(element)
    return len(se) == 1


N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(N):
    for d in range(D[i]):
        month = i + 1
        day = d + 1
        if is_ok(month, day):
            ans += 1
print(ans)
