result = []
def recursion(arr, idx, k, cur):
    global result
    if cur != [] and len(cur) ==  6:
        result.append(cur)
        return
    if idx == k: return
    recursion(arr, idx+1, k, cur + [arr[idx]]) 
    recursion(arr, idx+1, k, cur)

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0: break
    recursion(arr[1:], 0, k, [])
    for i in result:
        for j in i:
            print(j, end = " ")
    print('\n')
    result = []