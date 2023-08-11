def solution(n):
    answer = []
    k=10
    while n*10>=k:
        nn = n%k
        answer.append(nn//(k//10))
        k *= 10
    return answer

print(solution(12345))