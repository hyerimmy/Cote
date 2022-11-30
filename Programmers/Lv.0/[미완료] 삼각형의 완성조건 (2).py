def solution(sides):
    answer = list()
    sides.sort()
    for a in range(sides[1] - sides[0] + 1, sides[1]):
        if a not in answer:
            answer.append(a)
    for b in range(sides[0] + 1, sides[0] + sides[1]):
        if b not in answer:
            answer.append(b)
    return len(answer)


print(solution([11, 7]))
