# def solution(n):
#     answer = 0
#
#     for i in range(1,n+1):
#         if n%i == 0:
#             answer += i
#
#     return answer

def solution(n):
    answer = 0

    for i in range(1, int(n ** (1/2))+1):
        if n % i == 0:
            if n == i * i:
                answer += i
                break
            else:
                answer += i
                answer += n // i

    return answer


print(solution(12))
print(solution(5))
