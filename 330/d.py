N=int(input())
S=[input() for _ in range(N)]

row,col=[0 for _ in range(N)],[0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j]=='o':
            row[i]+=1
            col[j]+=1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j]=='o':
            zan_r = row[i]-1
            zan_c=col[j]-1
            ans+=zan_r*zan_c
print(ans)