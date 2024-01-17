from collections import deque
from heapq import heappop, heappush

import sys

inputs = sys.stdin.readline

"""再帰関数のときセット
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
"""

N = int(input())

node_info = [None] * N
node_info[0] = (1, 0, 0)
parent = [-1] * N
children = [[] for _ in range(N)]
for ni in range(1, N):
    p, t, s, g = map(int, input().split())
    node_info[ni] = (t, s, g)
    p -= 1
    parent[ni] = p
    children[p].append(ni)


def search(medicine, enemy, power):
    if len(medicine) == len(enemy) == 0:
        print("Yes")
        exit()
    nex_medicine = medicine[:]
    now_power = power
    enemy_que = []
    for v in enemy:
        t, s, g = node_info[v]
        heappush(enemy_que, (s, g, v))

    # 倒せる敵を全部倒す
    while enemy_que:
        s, g, v = heappop(enemy_que)
        if now_power < s:
            heappush(enemy_que, (s, g, v))
            break
        now_power += g
        for ch in children[v]:
            t, s, g = node_info[ch]
            if t == 1:
                heappush(enemy_que, (s, g, ch))
            else:
                nex_medicine.append(ch)

    # 倒せなかった敵を整理する
    nex_enemy = []
    while enemy_que:
        s, g, v = heappop(enemy_que)
        nex_enemy.append(v)

    if len(nex_medicine)==len(nex_enemy)==0:
        print("Yes")
        exit()

    # nex
    for med in nex_medicine:
        re_medicine = nex_medicine[:]
        re_medicine.remove(med)
        mu = node_info[med][2]
        re_enemy = nex_enemy[:]
        for ch in children[med]:
            t, s, g = node_info[ch]
            if t == 1:
                re_enemy.append(ch)
            else:
                re_medicine.append(ch)
        search(re_medicine, re_enemy, now_power * mu)


search([], [0], 1)
print("No")
