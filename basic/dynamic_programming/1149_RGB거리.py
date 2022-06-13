import sys
N = int(input())
price = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
total_price = [[0]*3 for _ in range(N)]
total_price[0] = price[0]
for i in range(1, N):
    total_price[i][0] = min(total_price[i-1][1], total_price[i-1][2]) + price[i][0]
    total_price[i][1] = min(total_price[i-1][0], total_price[i-1][2]) + price[i][1]
    total_price[i][2] = min(total_price[i-1][0], total_price[i-1][1]) + price[i][2]
print(min(total_price[N-1]))