def is_ok(x):
    str_x = str(x)
    a, b, c = str_x[0], str_x[1], str_x[2]
    return int(a) * int(b) == int(c)


N = int(input())
for x in range(N, 1000):
    if is_ok(x):
        print(x)
        break
