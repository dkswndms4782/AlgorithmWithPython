import sys
from collections import deque
N,K = map(int, sys.stdin.readline().split())
# if N==K: 
#     print(0)
#     sys.exit()
Max = 200000
seen = [False] * (Max + 1)
dist = [-1] * (Max + 1)
q = deque()
q.append(N)
seen[N] = True
dist[N] = 0
# 첫번째 버전
# time = 1
# while q:
#     now_level = len(q)
#     while now_level:
#         tmp = q.popleft()
#         if (tmp+1) == K or (tmp-1) == K or (tmp*2) == K:
#             print(time)
#             sys.exit()
#         if not seen[tmp*2] and tmp<=K:
#             seen[tmp*2] = True
#             q.append(tmp*2)
#         if not seen[tmp+1]:
#             seen[tmp+1] = True
#             q.append(tmp+1)
#         if not seen[tmp-1] and (tmp-1) >= 0:
#             seen[tmp-1] = True
#             q.append(tmp-1)
#         now_level -= 1
#     time += 1

# 두번째 버전
while q:
    now = q.popleft()
    for nxt in [now-1, now+1, now*2]:
        if 0<=nxt<=Max and seen[nxt] == False:
            seen[nxt] = True
            dist[nxt] = dist[now] + 1
            q.append(nxt)

print(dist[K])