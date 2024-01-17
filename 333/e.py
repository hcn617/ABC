from collections import defaultdict, deque

N = int(input())
query = [tuple(map(int, input().split())) for _ in range(N)]

dic = defaultdict(int)
portion = 0  # 持っているポーションの個数
ans = 0  # 持っているポーションの個数の最大値
ans_que = deque()
while query:
    t, x = query.pop()
    if t == 1:
        if dic[x] > 0:
            dic[x] -= 1
            portion -= 1
            ans_que.appendleft(1)
        else:
            ans_que.appendleft(0)
    elif t == 2:
        dic[x] += 1
        portion += 1
    ans = max(ans, portion)

if max(dic.values()) > 0:
    print(-1)
else:
    print(ans)
    print(*ans_que)
