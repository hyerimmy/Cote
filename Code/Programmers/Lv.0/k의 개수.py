def solution(i, j, k):
    answer = 0

    for n in range(i,j+1):
        for nn in str(n):
            if nn == str(k):
                answer += 1

    return answer

print(solution(1,13,1))