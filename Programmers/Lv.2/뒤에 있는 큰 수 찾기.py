# def solution(numbers):
#     answer = []
#     for index, number in enumerate(numbers):
#         numbers_behind = numbers[index:]
#
#         behind_number = -1
#         for number_behind in numbers_behind:
#             if number_behind > number:
#                 behind_number = number_behind
#                 break
#         answer.append(behind_number)
#
#     return answer

# def solution(numbers):
#     answer = [-1] * len(numbers)
#     stack_number_index = []
#
#     for index, number in enumerate(numbers):
#         for stack_index in stack_number_index.copy():
#             if numbers[stack_index] < number:
#                 stack_number_index.pop()
#                 answer[stack_index] = number
#         stack_number_index.append(index)
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack_index = []

    for index, number in enumerate(numbers):
        while stack_index and numbers[stack_index[-1]] < number:
            answer[stack_index.pop()] = number
        stack_index.append(index)
    return answer

print(solution([2, 3, 3, 5]	))
# print(solution([9, 1, 5, 3, 6, 2]	))
