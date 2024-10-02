def solution(id_list, report, k):
    report = list(set(report))
    mail = {v:0 for v in id_list}
    report_check = {v:[] for v in id_list}
    for r in report:
        a,b = r.split()
        report_check[b].append(a)
    for i in id_list:
        if len(report_check[i]) >= k:
            for j in report_check[i]:
                mail[j] += 1
    return list(mail.values())