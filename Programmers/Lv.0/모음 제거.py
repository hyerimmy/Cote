def solution(my_string):
    answer = ''
    for ms in my_string:
        if(ms=='a' or ms=='e' or ms=='i' or ms=='o' or ms=='u'):
            continue
        else:
            answer += ms
    return answer

print(solution("nice to meet you"	))