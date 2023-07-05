import sys

sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())


def dfs(lis, tail):
    if len(lis) == N:
        print(*lis)
        return

    for nex in range(tail + 1, M + 1):
        dfs(lis + [nex], nex)


dfs([], 0)
