def solution(my_string, n):
    answer = ''

    for ms in my_string:
        for _ in range(0,n):
            answer += ms

    return answer