import sys
from collections import deque
direction = [(1,0), (0,1), (-1,0), (0,-1)]
N,M = map(int, sys.stdin.readline().split())
result = [[100001]*M for _ in range(N)]
Maze = [[int(i) for i in sys.stdin.readline() if i != '\n'] for _ in range(N)]
q = deque()

def check(x,y):
    global N,M
    if x >= 0 and y >= 0 and x < N and y < M: return True
    return False

def BFS(a,b):
    global Maze, N, M, direction, result
    q.append((0,0))
    result[0][0] = 1
    while q:
        (a,b) = q.popleft()
        for i in direction:
            ax = i[0] + a
            bx = i[1] + b
            if check(ax,bx) and Maze[ax][bx] and (result[a][b] + 1 < result[ax][bx]):
                result[ax][bx] = result[a][b] + 1
                q.append((ax,bx))
                

BFS(0,0)
print(result[N-1][M-1])

