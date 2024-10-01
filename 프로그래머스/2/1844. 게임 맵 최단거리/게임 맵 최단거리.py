from collections import deque
# [0][1] -> 0
# 즉 앞 0은 row num
# 즉 뒤 1은 column num

direction = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs(start, q, visited, n, m, maps):
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        tmp = q.popleft()
        for d in direction:
            a, b = (tmp[0] + d[0]), (tmp[1] + d[1])
            if a<0 or a>=n or b<0 or b>=m: continue
            if maps[a][b]==0: continue
            if not visited[a][b]:
                if a==(n-1) and b==(m-1): return tmp[2]+1
                q.append((a,b,tmp[2]+1))
                visited[a][b] = True
    return -1
            
            
            
        
        
        

def solution(maps):
    q = deque()
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    start = (0,0,1)
    return bfs(start, q, visited, n, m, maps)
    
    