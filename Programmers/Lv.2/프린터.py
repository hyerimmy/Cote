def solution(priorities, location):
    answer = 0

    while priorities != []:
        num = priorities[0]

        if location == 0:
            if num == max(priorities):
                answer += 1
                return answer
            else:
                location = len(priorities)-1
        else:
            location -= 1

        if num != max(priorities):
            priorities.pop(0)
            priorities.append(num)
        else:
            priorities.pop(0)
            answer += 1

    return answer

print(solution([2, 1, 3, 2]	,2))
print(solution([1, 1, 9, 1, 1, 1],0))