# N과 K가 같을 때 exit()를 안해줌
# seen 크기 문제
# -로 좌표가 가는 문제
import sys
from collections import deque
N,K = map(int, sys.stdin.readline().split())
if N==K: 
    print(0)
    sys.exit()
seen = [False]*(1000001)
q = deque()
q.append(N)
seen[N] = True
time = 1
while q:
    now_level = len(q)
    while now_level:
        tmp = q.popleft()
        if (tmp+1) == K or (tmp-1) == K or (tmp*2) == K:
            print(time)
            sys.exit()
        if not seen[tmp*2] and tmp<=K:
            seen[tmp*2] = True
            q.append(tmp*2)
        if not seen[tmp+1]:
            seen[tmp+1] = True
            q.append(tmp+1)
        if not seen[tmp-1] and (tmp-1) >= 0:
            seen[tmp-1] = True
            q.append(tmp-1)
        now_level -= 1
    time += 1

