from collections import deque
M,N = map(int, input().split())
Maze = [list(map(int,list(input()))) for _ in range(N)]
q = deque([(0,0)])
seen = [[False] * M for _ in range(N)]
wall = [[0] * M for _ in range(N)]
seen[0][0] = True
direction = [(1,0),(0,1),(-1,0),(0,-1)]

while q:
    a,b = q.popleft()
    if Maze[a][b]: wall[a][b] += 1
    for i in direction:
        ax = a + i[0]
        bx = b + i[1]
        if 0<=ax<N and 0<=bx<M and not seen[ax][bx]:
            if Maze[ax][bx]: q.append((ax,bx))
            else: q.appendleft((ax,bx))
            seen[ax][bx] = True
            wall[ax][bx] = wall[a][b]

print(wall[N-1][M-1])