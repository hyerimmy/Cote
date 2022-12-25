def solution(quiz):
    answer = []

    for q in quiz:
        qq = q.split()

        if qq[1] == '+':
            ans = int(qq[0]) + int(qq[2])
        elif qq[1] == '-':
            ans = int(qq[0]) - int(qq[2])

        if int(qq[4]) == ans:
            answer.append("O")
        else:
            answer.append("X")

    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]	))