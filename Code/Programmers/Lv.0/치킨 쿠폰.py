def solution(chicken):
    answer = 0

    while chicken >= 10:
        newchicken = chicken // 10
        chicken = chicken % 10 + newchicken
        answer += newchicken

    return answer

print(solution(100))