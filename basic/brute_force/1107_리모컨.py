N = int(input())
M = int(input())
answer = 10000001
if M>0: 
    button = list(map(int, input().split()))
    bttn = [x for x in range(10) if x not in button]

def check(Num):
    global answer
    if ((len(f"{N}") + 1) < len(Num)): return
    elif ((len(f"{N}") -1) <= len(Num)) and ((len(f"{N}") + 1) >= len(Num)) and (len(Num) > 0):
        answer = min(answer, abs(N - int(Num)) + len(Num))
    if (len(Num) == 1) and (int(Num) == 0) : return
    if (len(f"{N}") !=6) or (len(f"{N}") == 6 and len(Num) < 6):
        for i in bttn:
            check(Num + f"{i}")


if __name__=="__main__":
    if M==10: print(abs(N-100))
    elif M==0: print(min(len(f"{N}"), abs(N-100)))
    else:
        check("")
        answer = min(answer, abs(N - 100))
        print(answer)

