import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
length = [1]*(N+1)
arr = [[]*(N+1) for _ in range(N+1)]
max_idx, max_length = 0,1
for i in range(0, N):
    prev = i
    for j in range(0, i):
        if A[i]>A[j] and length[i] < (length[j]+1):
            length[i] = length[j] + 1
            prev = j
    if max_length < length[i]: max_idx,max_length = i, length[i]
    if prev != i: arr[i].extend(arr[prev])
    arr[i].append(A[i])

print(max_length)
for i in arr[max_idx]: print(i, end=" ")
