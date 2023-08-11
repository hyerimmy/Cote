def solution(my_string):
    answer = []
    for ms in my_string:
        if(47<ord(ms)<58):
            answer.append(int(ms))
    answer.sort()
    return answer

print(solution("p2o4i8gj2"))