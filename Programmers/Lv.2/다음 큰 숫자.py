def solution(n):
    answer = n
    while 1:
        answer += 1
        if str(format(answer, 'b')).count('1') \
                == str(format(n, 'b')).count('1'):
            break
    return answer


print(solution(78))
print(solution(15))
