import sys
from collections import deque
M,N = map(int, sys.stdin.readline().split())
Box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Date = [[-1]*M for _ in range(N)]
q = deque()
direction = [(-1,0), (0,-1),(1,0), (0,1)]

def check(a,b):
    global N,M
    if a>=0 and b>=0 and a<N and b<M: return True
    return False

all_riped = True
for i in range(N):
    for j in range(M):
        if Box[i][j] == 1: 
            Date[i][j] = 0
            q.append((i,j))
        elif Box[i][j] == 0: all_riped = False
if all_riped: 
    print(0)
    sys.exit()

while q:
    now_level = len(q)
    while now_level:
        (a,b) = q.popleft()
        for i in direction:
            ax = a + i[0]
            bx = b + i[1]
            if check(ax,bx) and Box[ax][bx] == 0:
                Box[ax][bx] = 1
                Date[ax][bx] = Date[a][b] + 1
                q.append((ax,bx))
        now_level -= 1


all_riped = True
max_date = -1
for i in range(N):
    for j in range(M):
        if Box[i][j] == 0: all_riped = False
        if max_date < Date[i][j]: max_date = Date[i][j]

if not all_riped: print(-1)
else: print(max_date)
