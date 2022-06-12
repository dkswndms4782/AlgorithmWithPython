T = int(input())
N = [0]*12
N[1],N[2],N[3] = 1,2,4
for i in range(4,11):
    N[i] = N[i-1] + N[i-2] + N[i-3]
for i in range(T): print(N[int(input())])