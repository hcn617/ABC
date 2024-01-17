def repunit(length):
    return int('1' * length)


repunit3_lst = set()
for i in range(1, 13):
    for j in range(1, 13):
        for k in range(1, 13):
            value = repunit(i) + repunit(j) + repunit(k)
            repunit3_lst.add(value)

N = int(input())
print(sorted(repunit3_lst)[N - 1])
