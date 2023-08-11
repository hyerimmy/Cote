def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for k in range(i + 1, len(numbers)):
            result = numbers[i] + numbers[k]
            if result not in answer:
                answer.append(result)
    answer.sort()
    return answer


print(solution([5, 0, 2, 7]))
