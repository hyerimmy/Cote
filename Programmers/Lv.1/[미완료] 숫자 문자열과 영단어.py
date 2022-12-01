def solution(s):
    print(ord('0'))
    print(ord('1'))
    print(ord('9'))
    answer = 0
    new_s = list()
    for ss in s:
        if ord(ss) >= 48 and ord(ss) <= 57:
            new_s.append(ss)
    return answer

print(solution('1'))