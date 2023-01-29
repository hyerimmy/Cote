def solution(k, tangerine):
    answer = 0
    tcnt = dict()

    for t in tangerine:
        if t not in tcnt.keys():
            tcnt[t] = 1
        else:
            tcnt[t] += 1

    tval = sorted(tcnt.values(),reverse=True)

    for tv in tval:
        if k > 0:
            k -= tv
            answer += 1
        else:
            return answer

    return answer

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]	))