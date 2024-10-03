def solution(n):
    answer = [[0]*n for _ in range(n)]
    a,b = 0,0
    answer[a][b] = 1
    while True:
        while (b<n-1):
            if answer[a][b+1] == 0:
                b += 1
                answer[a][b] = answer[a][b-1]+1
            else: break
        while (a<n-1):
            if answer[a+1][b] == 0:
                a += 1
                answer[a][b] = answer[a-1][b]+1
            else: break
        while (b>0):
            if answer[a][b-1] == 0:
                b -= 1
                answer[a][b] = answer[a][b+1]+1
            else: break
        while (a>0):
            if answer[a-1][b] == 0:
                a -= 1
                answer[a][b] = answer[a+1][b]+1
            else: break
        if answer[a][b] == n*n: break
        
    return answer