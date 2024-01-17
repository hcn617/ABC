S = input()
ans = ""
for s in S:
    match s:
        case "a" | "e" | "i" | "o" | "u":
            pass
        case _:
            ans += s
print(ans)
