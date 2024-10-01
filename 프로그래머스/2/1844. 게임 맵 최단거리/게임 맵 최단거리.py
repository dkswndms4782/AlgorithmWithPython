from collections import deque

def solution(maps):
    q = deque([(0,0,1)])
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    direction = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        tmp = q.popleft()
        for d in direction:
            a, b = (tmp[0] + d[0]), (tmp[1] + d[1])
            if 0 <= a < n and 0 <= b < m:
                if not visited[a][b] and maps[a][b]==1:
                    if a==(n-1) and b==(m-1): return tmp[2]+1
                    q.append((a,b,tmp[2]+1))
                    visited[a][b] = True
    return -1
    
    