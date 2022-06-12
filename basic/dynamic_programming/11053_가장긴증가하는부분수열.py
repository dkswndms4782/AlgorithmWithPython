import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
length = [1]*(N+1)
for i in range(1,N):
    for j in range(0,i):
        if A[j] < A[i]: length[i] = max(length[i], length[j] + 1)
print(max(length))