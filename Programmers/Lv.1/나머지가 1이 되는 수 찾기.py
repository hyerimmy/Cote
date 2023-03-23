def solution(n):
    answer = 0

    for x in range(1,n):
        if n % x == 1:
            return x
    return answer

print(solution(10))
print(solution(12))
