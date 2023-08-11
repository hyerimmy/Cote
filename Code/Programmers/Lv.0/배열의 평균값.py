def solution(numbers):
    answer = 0
    for n in numbers:
        answer += n
    answer = answer/len(numbers)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))