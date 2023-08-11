def solution(array):
    answer = 0

    for a in array:
        for i in str(a):
            if i == '7':
                answer += 1

    return answer

array = [7, 77, 17]
print(solution(array))