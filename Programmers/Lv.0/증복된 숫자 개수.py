def solution(array, n):
    answer = 0
    for a in array:
        if (n==a):
            answer+=1
    return answer

print(solution([1, 1, 2, 3, 4, 5]	,1))