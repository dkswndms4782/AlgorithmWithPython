years = list(map(int, input().split()))

if __name__=="__main__":
    e,s,m = 1,1,1
    cnt = 1
    while [e,s,m] != years:
        e = (e+1) if e != 15 else 1
        s = (s+1) if s != 28 else 1
        m = (m+1) if m != 19 else 1
        cnt += 1
    print(cnt)
