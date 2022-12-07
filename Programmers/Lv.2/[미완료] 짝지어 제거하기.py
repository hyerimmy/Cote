def solution(s):
    while 1:
        if s == '':
            return 1
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                s = s.replace(s[i],"",2)
                break
            if i == len(s)-2:
                return 0



print(solution("0112345"))
print(solution("baabaa"))
print(solution("cdcd"))