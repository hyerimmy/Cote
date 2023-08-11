def solution(s):
    answer = s[0].upper()
    for i in range(0,len(s)-1):
        if s[i] == " ":
            answer += str(s[i+1]).upper()
        else:
            answer += str(s[i+1]).lower()
    return answer

print(solution("Hi OeWWpp po"))