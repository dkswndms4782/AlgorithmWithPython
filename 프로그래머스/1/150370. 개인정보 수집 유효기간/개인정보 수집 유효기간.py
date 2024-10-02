def solution(today, terms, privacies):
    term = {t.split()[0]:int(t.split()[1]) for t in terms}
    answer = []
    for i in range(len(privacies)):
        time, user = privacies[i].split()
        yt, mt, dt = map(int, time.split("."))
        valid = term[user]
        if (mt+valid) > 12:
            yt += (mt+valid)//12
            mt = (mt+valid)%12
            if mt==0: 
                mt=12
                yt-=1
        else: 
            mt += valid
        expire_date = f"{yt}." + (f"{mt}." if mt>9 else f"0{mt}.") + (f"{dt}" if dt>9 else f"0{dt}")
        if today >= expire_date:
            answer.append(i+1)
    return answer
        
        