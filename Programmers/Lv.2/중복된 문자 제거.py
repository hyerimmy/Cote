def solution(my_string):
    answer = ''

    for ms in my_string:
        if ms not in answer:
            answer += ms
    return answer

print(solution("people"))