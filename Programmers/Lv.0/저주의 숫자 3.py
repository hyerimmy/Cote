def solution(n):
    answer = 0
    for _ in range(0,n):
        answer += 1
        if '3' in str(answer) or answer%3 == 0:
            while '3' in str(answer) or answer%3 == 0:
                answer+=1
        # print(answer)

    return answer


print(solution(10))