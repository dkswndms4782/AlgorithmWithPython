import itertools
def solution(friends, gifts):
    give = {}
    gift_index = {}
    results = {}
    friends_group = list(itertools.combinations(friends,2))
    for i in friends_group:
        a,b = i[0],i[1]
        if a not in give.keys():
            give[a] = {}
        if b not in give.keys():
            give[b] = {}
        give[a][b] = 0
        give[b][a] = 0
    for f in friends:
        gift_index[f] = 0
        results[f] = 0
    for g in gifts:
        (a,b) = g.split()
        give[a][b] += 1
    for f in friends:
        gave = sum(give[f].values())
        got = 0
        for j in give.keys():
            if j==f: continue
            got += give[j][f]
        gift_index[f] = gave - got
    for i in friends_group:
        (a, b) = i
        if give[a][b] > give[b][a]:
            results[a] += 1
        elif give[a][b] < give[b][a]:
            results[b] += 1
        elif give[a][b]==give[b][a]:
            if gift_index[a]==gift_index[b]: continue
            if gift_index[a] > gift_index[b]:
                results[a] += 1
            elif gift_index[a] < gift_index[b]:
                results[b] += 1
    return max(results.values())
        
   