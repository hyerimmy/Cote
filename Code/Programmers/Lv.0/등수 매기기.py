def solution(score):
    answer = []

    avg = []

    for s in score:
        avg.append((s[0]+s[1])/2)

    print(avg)

    for i in range(0,len(avg)):
        answer.append(sorted(avg,reverse=True).index(avg[i])+1)

    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]	))