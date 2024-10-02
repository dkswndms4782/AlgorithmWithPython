def days(today):
    y,m,d = map(int, today.split("."))
    return y*12*28 + m*28 + d
def solution(today, terms, privacies):
    term = {t[0]:int(t[2:]) for t in terms}
    answer = []
    today = days(today)
    for i, priv in enumerate(privacies):
        priv_days = days(priv[:-2])
        contract_days = term[priv[-1]]*28
        if priv_days+contract_days <= today:
            answer.append(i+1)
    return answer
        
        