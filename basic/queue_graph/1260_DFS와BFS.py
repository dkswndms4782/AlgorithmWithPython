import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())
dfs_seen = [False] * (N+1) # 방문 했는지 체크 # node[3] = True
bfs_seen = [False] * (N+1)
q = deque()
# edge = [[]] * (N + 1) # 주소 복사가 돼서 모든 리스트가 같은 값을 가지게 됨. 

# 2번째 방법
#edge = [] # 간선이 있는지 체크 # edge[3] = [1,2,5]
# 새 주소의 빈 배열 넣음
#for i in range(N+1): 
#    edge.append([])

# 3번째 방법
edge = [[] for _ in range(N+1)]

def DFS(V):
    global dfs_seen, edge
    print(V, end=' ')
    dfs_seen[V] = True
    for i in edge[V]:
        if not dfs_seen[i]: 
            DFS(i)

# 이전 버전        
# def BFS(V):
#     global bfs_seen, edge, q
#     q.append(V)
#     print(V, end=" ")
#     bfs_seen[V] = True
#     while True:
#         if len(q) == 0: return
#         tmp = q.popleft()
#         for i in edge[tmp]:
#             if not bfs_seen[i]: 
#                 q.append(i)
#                 print(i, end=" ")
#                 bfs_seen[i] = True

def BFS(V):
    global bfs_seen, edge, q
    q.append(V)
    bfs_seen[V] = True
    while q:
        tmp = q.popleft()
        print(tmp, end=" ")
        for i in edge[tmp]:
            if not bfs_seen[i]: 
                q.append(i)
                bfs_seen[i] = True


if __name__ == "__main__":
    for i in range(M):
        a,b = map(int, sys.stdin.readline().split())
        edge[a].append(b)
        edge[b].append(a)
    for i in range(N+1): edge[i].sort()
    DFS(V)
    print('')
    BFS(V)