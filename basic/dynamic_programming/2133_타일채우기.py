# 세상에 이거 내힘으로 푼 부분이 없음 다시 한번 더 풀어라
N = int(input())
dp = [0] * 31
dp[0],dp[2],dp[4] = 1,3,11
for i in range(6,31,2):
    now = 0
    while now != i:
        if now == (i-2): dp[i] += 3*dp[now]
        else: dp[i] += 2 * dp[now]
        now += 2
print(dp[N])