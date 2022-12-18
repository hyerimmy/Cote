def solution(emergency):
    answer = []

    for e in emergency:
        answer.append(
            sorted(emergency,reverse=True).index(e)+1)

    return answer

print(solution([3, 76, 24]	))