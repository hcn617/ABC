V = {'R': (1, 0),
     'L': (-1, 0),
     'U': (0, 1),
     'D': (0, -1)
     }

N, Q = map(int, input().split())

lst = [(i, 0) for i in range(1, N + 1)]
lst = lst[::-1]
for _ in range(Q):
    t, q = input().split()
    if t == '1':
        vx, vy = V[q]
        prev_x, prev_y = lst[-1]
        new_x, new_y = prev_x + vx, prev_y + vy
        lst.append((new_x, new_y))
    else:
        print(*lst[-int(q)])
