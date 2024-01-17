# 2つの文字列の長さがおなじとき
def judge1(A, B):
    diff_cnt = 0
    for a, b in zip(A, B):
        if a != b:
            diff_cnt += 1
    return diff_cnt <= 1


# 2つの文字列の長さが1つちがいのとき
def judge2(A, B):
    if len(A) > len(B):
        A, B = B, A
    j = 0
    for i in range(len(A)):
        if A[i] == B[j]:
            j += 1
            continue
        j += 1
        if i + 1 != j:
            return False
        if A[i] == B[j]:
            j += 1
        else:
            return False
    return True


N, T = input().split()
N = int(N)
ans_lst = []

for i in range(1, N + 1):
    S = input()
    if len(S) == len(T):
        if judge1(S, T): ans_lst.append(i)
    elif abs(len(S) - len(T)) == 1:
        if judge2(S, T): ans_lst.append(i)

print(len(ans_lst))
print(*ans_lst)
