# t:00 に会議を開始するときの、会議の参加人数
def f(t):
    cnt = 0
    for w, x in wx:
        time = (x + t) % 24
        if 9 <= time <= 17:
            cnt += w
    return cnt


N = int(input())
wx = [list(map(int, input().split())) for _ in range(N)]

ans = max(f(t) for t in range(24))
print(ans)
