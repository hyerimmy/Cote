from itertools import combinations

def factorial(n):
    result = 1
    if n > 1:
        for i in range(1,n+1):
            result *= i
    return result

def solution(balls, share):
    answer = factorial(balls) // factorial(share) // factorial(balls-share)
    return answer

print(solution(3,2))
print(solution(5,3))