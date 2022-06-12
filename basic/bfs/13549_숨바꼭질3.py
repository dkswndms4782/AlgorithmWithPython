from collections import deque
N,K = map(int, input().split())
Max = 200000
q = deque()
q.append(N)
seen = [False]*(Max+1)
seen[N] = True
dist = [-1]*(Max+1)
dist[N] = 0
while q:
    now = q.popleft()
    if 0<= now*2 <= Max and not seen[now*2]:
        seen[now*2] = True
        q.appendleft(now*2)
        dist[now*2] = dist[now]
    for nxt in [now+1, now-1]:
        if 0<=nxt<=Max and not seen[nxt]:
            seen[nxt] = True
            q.append(nxt)
            dist[nxt] = dist[now] + 1
print(dist[K])