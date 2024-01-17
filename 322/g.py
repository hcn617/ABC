from collections import defaultdict
from heapq import heappop, heappush

N, M = map(int, input().split())
S = [input() for _ in range(N)]

T = [[] * 10 for _ in range(N)]

for i in range(N):
    for j in range(M):
        el = int(S[i][j])
        T[i][el].append(j)

ans = 1 << 50
for j in range(10):
    is_ok = True
    for i in range(N):
        if len(T[i][j]) == 0:
            is_ok = False
            break
    if not is_ok:
        continue

    look_idx = [0] * N
    dic = defaultdict(list)
    sinonim = []
    sinonim_node = [[] for _ in range(N)]
    push_time = [-1] * N
    time_que = []
    for i in range(N):
        dic[T[i][j][0]].append(i)
        if len(dic[T[i][j][0]]) == 1:
            heappush(time_que, T[i][j][0])
    while time_que:
        time = heappop(time_que)
        if len(dic[time]) == 1:
            push_time[dic[time].pop()] = time
        else:
            sinonim_code = len(sinonim)
            sinonim.append((time, dic[time]))

            for v in dic[time]:
                look_idx[v] += 1
                look_idx[v] %= len(T[v][j])
