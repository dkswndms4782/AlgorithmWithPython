N = int(input())
arr = [[0,0]] # ù��° : ���Ⱓ �ι�° : ����
for _ in range(N): arr.append(list(map(int, input().split())))
money = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, i):
        if (j + arr[j][0]) <= i: money[i] = max(money[j], money[i])
    if (i + arr[i][0]) <= (N+1): money[i] += arr[i][1]
print(max(money))