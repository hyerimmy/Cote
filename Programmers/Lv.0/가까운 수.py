def solution(array, n):
    array.sort()

    answer = array[0]
    answer_gap = (array[0]-n)*(array[0]-n)

    for a in array:
        if (a-n)*(a-n) < answer_gap:
            answer_gap = (a-n)*(a-n)
            answer = a

    return answer

print(solution([3, 10, 28]	,20))
print(solution([3, 10, 20]	,15))
print(solution([3, 12, 20]	,15))
print(solution([15, 12, 20]	,15))
print(solution([15, 12, 20]	,12))
print(solution([20, 21, 19,19]	,15))