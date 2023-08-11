def solution(n):
    answer = 0

    for nn in str(n):
        answer+=int(nn)

    return answer

print(solution(1234))