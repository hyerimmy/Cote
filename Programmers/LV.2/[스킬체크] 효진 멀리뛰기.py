def solution(n):
    answer = 0
    max = n//2
    for two in range(0,max+1):
        one = n-2*two
        answer += factorial(one+two)//(factorial(one)*factorial(two))
    return answer

def factorial(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

print(solution(4))
print(solution(3))