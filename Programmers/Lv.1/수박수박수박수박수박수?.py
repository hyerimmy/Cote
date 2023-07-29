def solution(n):
    answer = ''
    for _ in range(0,n//2):
        answer += "수박"
    if n%2==1:
        answer += "수"

    return answer

print(solution(3))
print(solution(4))
바