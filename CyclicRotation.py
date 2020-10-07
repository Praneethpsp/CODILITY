def solution(a,k):
    if a==[] or k==0:
        return a
    else:
        for count in range(0, k):
            x = []
            temp = a[-1]
            x.append(temp)
            for i in range(len(a) - 1):
                x.append(a[i])
            a = x
        return a

print(solution([],18))
