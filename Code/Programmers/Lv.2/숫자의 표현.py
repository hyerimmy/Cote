def solution(n):
    answer = 0
    for start in range(1,n+1):
        sumnum = 0
        for middle in range(start,n+1):
            sumnum += middle
            if sumnum == n:
                answer += 1
            elif sumnum > n:
                break
    return answer

print(solution(15))