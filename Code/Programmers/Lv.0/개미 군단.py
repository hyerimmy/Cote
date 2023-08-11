def solution(hp):
    answer = 0

    for ant in [5,3,1]:
        answer += hp//ant
        hp %= ant

    return answer

print(solution(23))
print(solution(24))
print(solution(999))