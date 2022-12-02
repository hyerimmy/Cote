def solution(n, lost, reserve):
    answer = 0

    student = [0] * (n + 2)

    for l in lost:
        student[l] -= 1
    for r in reserve:
        student[r] += 1

    for i in range(1, len(student)):
        if (student[i] == 1):
            if (student[i - 1] == -1):
                student[i - 1] += 1
                student[i] -= 0
            elif (student[i + 1] == -1):
                student[i + 1] += 1
                student[i] -= 0

    for s in range(1,len(student)-1):
        if student[s] >= 0:
            answer += 1

    return answer

print(solution(	5, [2, 4], [1, 3, 5]))