def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = -1
    while i < len(people):
        i += 1
        print("i",i)
        sum = people[i]
        if i+1 < len(people):
            while sum+people[i+1] <= limit:
                i += 1
                sum += people[i]
                if i+1 <= len(people):
                    break
            answer += 1
    return answer

print(solution([70, 50, 80, 50],100))