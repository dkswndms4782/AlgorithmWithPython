N = int(input())
road = [list(map(int, input().split())) for _ in range(N)]
seen = [False]*N
result = 100000001

def recursion(now, cal, cnt):
    global result, seen
    seen[now] = True
    if cnt == N and road[now][0] != 0:
        result = min(result, cal + road[now][0])
        seen[now] = False
        return
    for i in range(N):
        if not seen[i] and road[now][i] != 0:
            recursion(i, cal + road[now][i],cnt+1)
    seen[now] = False

recursion(0,0,1)
print(result)