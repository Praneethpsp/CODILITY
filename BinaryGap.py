def solution(N):
    binary=bin(N).replace('0b',"")
    binary=list(str(binary))
    result=0
    res=0
    for i in range(len(binary)):
        if '1' in binary:
            start = binary.index('1')
            binary[start] = 'a'
            if '1' in binary:
                end = binary.index('1')
                result = (end - start) - 1
                if result > res:
                    res = result
    return res

print(solution(805306373))