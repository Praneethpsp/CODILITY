def solution(a):
    if len(a) == 1:
        return a[0]
    a.sort()
    for i in range(0, len(a), 2):
        if i + 1 == len(a):
            return a[i]
        if a[i] != a[i + 1]:
            return a[i]


print(solution([4, 4, 4, 3, 3, 4, 3, 3, 4, 5]))
