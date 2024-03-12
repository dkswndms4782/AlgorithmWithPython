from collections import deque
def solution(s):
    answer = True
    stack = deque()
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if len(stack)==0:
                answer = False
                break
            else:
                stack.pop()
    if len(stack) > 0: answer = False
    return answer