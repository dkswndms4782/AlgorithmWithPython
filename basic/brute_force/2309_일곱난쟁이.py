friends = []
for i in range(9): friends.append(int(input()))

if __name__=="__main__":
    sum = sum(friends)
    for i in range(9):
        flag = False
        for j in range(i+1, 9):
            if (sum -friends[i] - friends[j]) == 100:
                # del arr[1] or arr.remove(arr[1])
                del friends[i],friends[j-1]
                # a.sort() or a = sorted(a)
                friends.sort()
                flag = True
                break
        if flag: break
    for i in friends: print(i)
