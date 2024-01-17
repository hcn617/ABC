# 半分全列挙。向きの正負のリストを返す。
def middle_tec(lst, x):
    lst1, lst2 = [], []
    for i, el in enumerate(lst):
        if i + i < len(lst):
            lst1.append(el)
        else:
            lst2.append(el)
    dic1, dic2 = state_dict(lst1), state_dict(lst2)
    for key1 in dic1.keys():
        if (key2 := x - key1) in dic2:
            vec = []
            state1, state2 = dic1[key1], dic2[key2]
            for i in range(len(lst1)):
                vec.append((state1 >> i) & 1)
            for i in range(len(lst2)):
                vec.append((state2 >> i) & 1)
            return vec
    print("No")
    exit()


# 符号を変えてつくれる値を全探索する。key:値 value:state になってるdictを返す。
def state_dict(lst):
    dic = dict()  # dic[value] = state
    for state in range(1 << len(lst)):
        val = 0
        for i, el in enumerate(lst):
            if (state >> i) & 1:
                val += el
            else:
                val -= el
        dic[val] = state
    return dic


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

x_lst, y_lst = [], []
for i, a in enumerate(A):
    if i % 2 == 1:
        x_lst.append(a)
    else:
        y_lst.append(a)
vec_x, vec_y = middle_tec(x_lst, X), middle_tec(y_lst, Y)
prev_vec = 1
ans_lst = []
for i in range(N):
    now_vec: int
    if i & 1:
        now_vec = vec_x[i // 2]
        match prev_vec, now_vec:
            case 1, 1: ans_lst.append('R')
            case 0, 0: ans_lst.append('R')
            case 1, 0: ans_lst.append('L')
            case 0, 1: ans_lst.append('L')

    else:
        now_vec = vec_y[i // 2]
        match prev_vec, now_vec:
            case 1, 1: ans_lst.append('L')
            case 0, 0: ans_lst.append('L')
            case 1, 0: ans_lst.append('R')
            case 0, 1: ans_lst.append('R')
    prev_vec = now_vec

print("Yes")
print(*ans_lst, sep='')
