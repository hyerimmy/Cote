def solution(order):
    answer = 0
    clap = ['3','6','9']

    for o in str(order):
        if o in clap:
            answer += 1
    return answer

print(solution(29423))