Max = 1000001
div = 1000000009
N = [0]*Max
N[1],N[2],N[3] = 1,2,4
for i in range(4, Max):
    N[i] = (N[i-1]%div + N[i-2]%div + N[i-3]%div) % div

T = int(input())
for _ in range(T): print(N[int(input())])