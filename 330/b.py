def f(a):
    if a <= L:
        return L
    if R <= a:
        return R
    return a


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans_lst = [f(a) for a in A]
print(*ans_lst)


