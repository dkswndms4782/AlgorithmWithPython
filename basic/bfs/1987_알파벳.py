from collections import deque
direction = [(1,0),(0,1),(-1,0),(0,-1)]
R,C = map(int,input().split())
board = [input() for _ in range(R)]
seen = [[False]*C for _ in range(R)]
alphabet = [False]*100
#q = deque()
result = 1

def DFS(a,b,c):
    global seen, q, result
    seen[a][b] = True
    # q.append(board[a][b])
    alphabet[ord(board[a][b])] = True
    result = max(c, result)
    for i in direction:
        ax,bx = (a+i[0]),(b+i[1])
        # if 0<=ax<R and 0<=bx<C and board[ax][bx] not in q:
        if 0<=ax<R and 0<=bx<C and not alphabet[ord(board[ax][bx])]:
            DFS(ax,bx,c+1)
    seen[a][b] = False
    # q.pop()
    alphabet[ord(board[a][b])] = False

DFS(0,0,1)
print(result)