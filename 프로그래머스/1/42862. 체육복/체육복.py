def solution(n, lost, reserve):
    re = sorted([i for i in reserve if i not in lost])
    lo = sorted([i for i in lost if i not in reserve])
    for r in re:
        a = r-1
        b = r+1
        if a in lo:
            lo.remove(a)
            continue
        if b in lo:
            lo.remove(b)
            continue
    return n - len(lo)
            