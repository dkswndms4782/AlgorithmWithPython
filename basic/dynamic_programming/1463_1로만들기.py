X = int(input())
N = [0] * (1000001)
N[2],N[3],N[4] = 1,1,2
for i in range(5, X+1):
    N[i] = N[i-1]+1
    if i%2 == 0: N[i] = min(N[i], N[i//2] + 1)
    if i%3 == 0: N[i] = min(N[i], N[i//3] + 1)
print(N[X])
