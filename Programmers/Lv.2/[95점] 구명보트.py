import math
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        if people[0] > limit / 2 or len(people) == 1:
            answer += len(people)
            break
        if people[-1] <= limit / 2:
            answer += math.ceil(len(people) / 2)
            break

        amount = people.pop()
        if not ((amount + people[0]) > limit):
            new_people = deque()
            for idx, new_amount in enumerate(people):
                if amount + new_amount <= limit:
                    people.popleft()
                    new_people.extend(people)
                    break
                else:
                    new_people.append(people.popleft())
            people = new_people
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

print(solution([10,20,30,40], 100))
print(solution([10,20,30,40,50], 100))
