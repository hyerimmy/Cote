def solution(my_string, letter):
    answer = ''
    for ms in my_string:
        if (ms!=letter):
            answer+=ms
    return answer