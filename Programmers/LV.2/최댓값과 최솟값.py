def solution(s):
    slist = sorted(list(map(int, s.split())))
    answer = str(slist[0])+" "+str(slist[-1])
    return answer

print(solution("5 2 3 4"))