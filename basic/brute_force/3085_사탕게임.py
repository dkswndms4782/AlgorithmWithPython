N = int(input())
Map = [[j for j in input()] for i in range(N)]
ans = 0

def count_row(a):
    global ans
    now = Map[a][0]
    cnt = 1
    for i in range(1,N):
        if now == Map[a][i]: cnt += 1
        else:
            now = Map[a][i]
            if ans < cnt: ans = cnt
            cnt = 1
    if ans < cnt: ans = cnt

def count_column(b):
    global ans
    now = Map[0][b]
    cnt = 1
    for i in range(1,N):
        
        if now == Map[i][b]: cnt += 1
        else:
            now = Map[i][b]
            if ans < cnt: ans = cnt
            cnt = 1
    if ans < cnt: ans = cnt

def change_row():
    for i in range(N):
        for j in range(N-1):
            Map[i][j], Map[i][j+1] = Map[i][j+1], Map[i][j]
            count_row(i)
            count_column(j)
            count_column(j+1)
            Map[i][j], Map[i][j+1] = Map[i][j+1], Map[i][j]

def change_column():
    for i in range(N-1):
        for j in range(N):
            Map[i][j], Map[i+1][j] = Map[i+1][j], Map[i][j]
            count_column(j)
            count_row(i)
            count_row(i+1)
            Map[i][j], Map[i+1][j] = Map[i+1][j], Map[i][j]

if __name__=="__main__":
    for i in range(N):
        count_column(i)
        count_row(i)
    change_column()
    change_row()
    print(ans)
