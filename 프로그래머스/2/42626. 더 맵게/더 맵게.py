import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while(True):
        if scoville[0] >= K: return answer
        a,b = hq.heappop(scoville), hq.heappop(scoville)
        tmp = (a+b*2)
        hq.heappush(scoville, tmp)
        answer += 1
        if len(scoville)==1 and scoville[0]<K: return -1
        
        