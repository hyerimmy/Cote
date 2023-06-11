def solution(numbers):
    numbers.sort(key=str, reverse=True)
    answer = ""
    for _ in range(len(numbers)):
        if not numbers:
            break
        if numbers[0] < 10:
            answer += str(numbers.pop(0))
        else:
            first_number = int(str(numbers[0])[0])
            if first_number in numbers:
                new_number_1 = str(numbers[0])
                new_number_2 = str(first_number) + str(numbers[0])
                if new_number_1 < new_number_2:
                    answer += str(first_number) + str(numbers.pop(0))
                    numbers.remove(first_number)
                    continue
            answer += str(numbers.pop(0))
    return answer

print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
