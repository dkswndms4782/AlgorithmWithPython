N = int(input())
pinary = [[0] * 2 for _ in range(91)]
pinary[1][0], pinary[1][1] = 0,1
for i in range(2,91):
    pinary[i][0] = pinary[i-1][0] + pinary[i-1][1]
    pinary[i][1] = pinary[i-1][0]
print(pinary[N][0] + pinary[N][1])