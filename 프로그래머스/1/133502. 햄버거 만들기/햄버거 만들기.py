def solution(ingredient):
    answer = 0
    q = []
    for i in ingredient:
        q.append(i)
        if q[-4:] == [1,2,3,1]:
            answer+=1
            for _ in range(4): q.pop()
    return answer