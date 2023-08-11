def solution(begin, end):
    answer = [None]*(end-begin+1)

    k = end//2

    for num in range(end,begin-1,-1):
        if num == 1:
            answer[num-1] = 0
        for kk in range(1,k+1):
            if num % kk == 0 and num > kk:
                answer[num-begin] = kk
    return answer


print(10**2)
print(solution(1,10))
print(solution(2,10))
