N = int(input())
A = [int(t) - 1 for t in input().split()]

seen_list = [0]
se = {0}  # seen_list のセット
v = 0
while True:
    nv = A[v]
    if nv not in se:
        se.add(nv)
        seen_list.append(nv)
        v = nv
    else:
        idx = seen_list.index(nv)
        ans_list = seen_list[idx:]
        print(len(ans_list))
        print(*[a + 1 for a in ans_list])
        break
