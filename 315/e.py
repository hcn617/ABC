import sys
import pypyjit

sys.setrecursionlimit(10 ** 7)
pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
G = []
for i in range(N):
    c, *p = map(lambda x: int(x) - 1, input().split())
    G.append(p)

read = [False] * N  # read[i]:本iを読んだことがあればTrue
ans_lst = []


def dfs(v):
    if not read[v]:
        for nv in G[v]:
            if read[nv]:
                continue
            dfs(nv)
            read[nv] = True
            ans_lst.append(nv + 1)


dfs(0)
print(*ans_lst)
