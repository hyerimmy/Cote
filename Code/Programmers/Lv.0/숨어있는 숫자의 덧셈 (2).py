def solution(my_string):
    answer = 0
    num = ''
    for i in my_string:
        if (97 <= ord(i) <= 122 or 65 <= ord(i) <= 90):
            if (num != ''):
                answer += int(num)
            num = ''
        else:
            num += i
    if (num != ''):
        answer += int(num)
    return answer


print(solution("12"))
