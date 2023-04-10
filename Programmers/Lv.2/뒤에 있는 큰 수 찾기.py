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

def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    print(stack)
    for i, number in enumerate(numbers):
        print("<<num>>",number)
        print(stack)
        print("answer",answer)
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)
    return answer

print(solution([2, 3, 3, 5]	))
# print(solution([9, 1, 5, 3, 6, 2]	))
