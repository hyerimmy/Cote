def solution(n):
    answer = 0

    for nn in range(1,n+1):
        if n%nn == 0:
            answer += 1
    return answer