N,S = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

def recursion(idx, sum, flag):
    global result
    if sum == S and flag: 
        result += 1
    if idx == N: return
    recursion(idx+1, sum+arr[idx], True)
    recursion(idx+1, sum, False)

recursion(0,0,False)
print(result)
