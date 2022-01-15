N = input()
answer = 0
for i in range(1, len(N)):
    answer += (10**i - 10**(i-1))*i
answer += ((int(N) - 10**(len(N)-1))+ 1)*len(N) 
print(answer)