def solution(n):
    answer = 1 # 2의 개수가 0개일 경우의 수 1개
    max_2count = n//2

    for m2c in range(1,max_2count+1):
        counting = factorial(n-m2c)//factorial(m2c)//factorial(n-2*m2c)
        answer += counting % 1234567

    return answer % 1234567

def factorial(n):
    if n < 2:
        return 1
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

testcase = [4, 3, 1]
for tc in testcase:
    print("solution(",tc,") = ",solution(tc))