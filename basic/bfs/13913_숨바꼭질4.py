from collections import deque
N,K = map(int, input().split())
if N == K: 
    print(f"0\n{N}") 
    exit()
Max = 200001
q = deque()
q.append(N)
seen = [False] * (Max + 1)
seen[N] = True
cor = [-1] * (Max + 1)

# assigning values to the list each time is inefficient. let's take the coordinates
while cor[K] == -1:
    now = q.popleft()
    for nxt in [now+1, now-1, now*2]:
        if 0<=nxt<=Max and not seen[nxt]:
            q.append(nxt)
            seen[nxt] = True
            cor[nxt] = now
            
tmp = K
result = []
while tmp != N:
    result.append(tmp)
    tmp = cor[tmp]
result.append(N)
result.reverse()
print(len(result) - 1)
for i in result: print(i, end = " ")

"""
while True:
    now = q.popleft()
    if now == K:
        print(len(seen[K])-1)
        for i in seen[K]: print(i, end = ' ')
        break
    if 0 <= now*2 <= MAX and len(seen[now*2]) == 0:
        q.append(now*2)
        # seen[now*2].extend(seen[now] + [now*2])
        # Extend has a time complexity of O(k). Where k is the length of the list which need to be added.
        # a = a + [100001] => O(N)
        # a += [4,5,6] => O(K)

        # assigning values each time is inefficient. let's take the coordinates
        seen[now*2] = seen[now] + [now*2]
    for nxt in [now+1, now-1]:
        if 0 <= nxt <= MAX and len(seen[nxt]) == 0:
            # append is O(1)
            q.append(nxt)
            seen[nxt] = seen[now] + [nxt]
    seen[now] = [now] 
    # clear is O(n) for a list with n elements
    # While CPython's list.clear has to touch every element to avoid a memory leak, it is quite possible that PyPy's garbage collector never needs to do anything of the sort, and thus has a true O(1) list.clear.
"""