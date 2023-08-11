def solution(lines):
    answer = 0
    line_history = []
    line_answer_history = []

    for l in lines:
        for i in range(l[0],l[1]):
            if i not in line_history:
                line_history.append(i)
            else:
                if i not in line_answer_history:
                    answer += 1
                    line_answer_history.append(i)
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]	))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))