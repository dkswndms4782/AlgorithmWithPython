import sys
T = int(sys.stdin.readline())
while(T != 0):
    calender = list(map(int, sys.stdin.readline().split()))
    flag = [[False] * (calender[1] + 1)] * (calender[0] + 1)
    x,y,cnt = 1,1,1

    y += (abs(calender[2] - x)) % calender[1]
    cnt += abs(calender[2] - x)
    x = calender[2]
        
    while True:
        if calender[2] == 1 and calender[3] == 1: break
        if y == calender[3]: break
        y += calender[0]
        cnt += calender[0]
        y = y if y <= calender[1] else y % calender[1]
        if y == 0: y += calender[1]
        if flag[x][y]:
            cnt = -1
            break
        flag[x][y] = True
    print(cnt)
    T-=1


