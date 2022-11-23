def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer

print(solution([1, 2, 7, 10, 11]))