def solution(x, n):
    answer = []
    num = x
    while len(answer) < n:
        answer.append(num)
        num += x
    return answer

print(solution(2,5))