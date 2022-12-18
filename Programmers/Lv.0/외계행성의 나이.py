def solution(age):
    alist = list(str(age))
    result = ''

    for al in alist:
        result += chr(ord(al)+49)
    return result

print(solution(23))
