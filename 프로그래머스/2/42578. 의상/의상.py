dict = {}
def solution(clothes):
    for i in clothes:
        if i[1] not in dict.keys():
            dict[i[1]] = []
        dict[i[1]].append(i[0])
    answer = 1
    for key in dict.keys():
        answer *= len(dict[key])+1
    answer-=1
    return answer