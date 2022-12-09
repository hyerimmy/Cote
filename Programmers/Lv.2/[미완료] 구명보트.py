def solution(people, limit):
    answer = 0
    people.sort()

    sum = 0
    for p in people:

        if sum + p <= limit:
            sum += p
        else:
            sum = p
            answer += 1

    return answer+1


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
