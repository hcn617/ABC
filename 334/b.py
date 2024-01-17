A, M, L, R = map(int, input().split())

left = (L - A) // M
if (L - A) % M != 0:
    left += 1

right = (R - A) // M
print(right - left + 1)
