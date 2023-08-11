def solution(s):
    answer = [0,0]
    while s != '1':
        answer[1] += s.count('0')
        answer[0] += 1
        if(s.count('0')>0):
            s = s.replace('0',"",s.count('0'))
        s = format(len(s),'b')
    return answer

print(solution("110010101001"))