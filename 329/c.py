from itertools import groupby
from collections import defaultdict

N = int(input())
S = input()

dic = defaultdict(int)
for el, group in groupby(S):
    dic[el] = max(dic[el], len(list(group)))
print(sum(dic.values()))
