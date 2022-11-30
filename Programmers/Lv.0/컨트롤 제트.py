def solution(s):
    answer = 0
    slist = s.split()
    for i in range(0, len(slist)):
        if (slist[i] == 'Z'):
            answer -= int(slist[i - 1])
        else:
            answer += int(slist[i])
    return answer
