from collections import  deque
def solution(people, limit):
    answer = 0
    people.sort()

    people = deque(sorted(people))

    while people:
        k = people.pop()
        if people:
            if people[0] + k <= limit:
                people.popleft()
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

print(solution([10,20,30,40], 100))
print(solution([10,20,30,40,50], 100))
