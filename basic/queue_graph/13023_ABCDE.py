import sys
N,M = map(int, sys.stdin.readline().split())
seen = [False] * N
edge = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

def DFS(cur_node, depth):
    global edge, seen
    if depth >= 5: 
        return True
    seen[cur_node] = True
    flag = False
    for i in edge[cur_node]:
        if not seen[i]:
            if DFS(i, depth+1): flag = True
    seen[cur_node] = False
    return flag


for cur_node in range(N):
    if DFS(cur_node, 1): 
        print(1)
        sys.exit()
print(0)

