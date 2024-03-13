from collections import deque
def solution(operations):
    minv, maxv, queue = 10000001, -10000001, deque()
    for operation in operations:
        commend = operation[0]
        value = int(operation[2:])
        
        if commend =='D':
            if len(queue)==0: continue
            if value==1: 
                queue.pop()
            elif value==-1: queue.popleft()
        elif commend=='I':
            if maxv < value: 
                queue.append(value)
                maxv = value
                if minv > value: minv = value
            elif minv > value:
                queue.appendleft(value)
                minv = value
                if maxv < value : maxv = value
            else:
                queue.append(value)
                queue = deque(sorted(queue))
        print(minv, maxv)
    if len(queue)==0: return [0,0]
    else: return [queue[-1], queue[0]]