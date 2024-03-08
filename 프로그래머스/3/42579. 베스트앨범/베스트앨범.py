genres_dict = {}
plays_dict = {}
def solution(genres, plays):
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genres_dict.keys():
            genres_dict[genre] = []
        genres_dict[genre].append(play)
        if play not in plays_dict.keys():
            plays_dict[play] = []
        plays_dict[play].append(idx)
    
    genres_keys = sorted(genres_dict, key=lambda k: sum(genres_dict[k]), reverse=True)
    for key in genres_keys:
        genres_dict[key] = sorted(genres_dict[key], reverse=True)
    for key in plays_dict.keys():
        plays_dict[key] = sorted(plays_dict[key])
    
    answer, count = [],0
    for key in genres_keys:
        for plays_key in genres_dict[key]:
            for idx in plays_dict[plays_key]:
                answer.append(idx)
                count+=1
                if count==2:break
            if count==2: break
        count = 0
    
    return answer