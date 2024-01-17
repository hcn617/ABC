from heapq import heappop, heappush
from collections import deque

N, M = map(int, input().split())

somen_que = deque()
for _ in range(M):
    t, w, s = map(int, input().split())
    somen_que.append((t, w, s))

human_comeback_que = []
human_wait_list = []
for i in range(N):
    heappush(human_wait_list,i)
ans_lst = [0] * N
while somen_que:
    t, w, s = somen_que.popleft()
    while human_comeback_que:
        ht, hi = heappop(human_comeback_que)
        if ht <= t:
            heappush(human_wait_list, hi)
        else:
            heappush(human_comeback_que, (ht, hi))
            break
    if len(human_wait_list) == 0:
        continue
    hi = heappop(human_wait_list)
    ans_lst[hi] += w
    heappush(human_comeback_que, (t + s, hi))

for ans in ans_lst:
    print(ans)
