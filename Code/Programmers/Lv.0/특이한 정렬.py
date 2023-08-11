def solution(numlist, n):
    return(sorted(numlist, key=lambda x: (abs(n-x),-x)))


print(solution([1, 2, 3, 4, 5, 6]	,4))