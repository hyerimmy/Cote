def solution(scoville, K):
    answer = 0
    scoville.sort()

    while scoville[0] < K:
        # print(scoville)
        if len(scoville) < 2:
            return -1
        if scoville[1] < K:
            new_scoville = scoville.pop(0) + scoville.pop(0)*2
            scoville.append(new_scoville)
            scoville.sort()
        else:
            new_scoville = scoville.pop(0) + scoville.pop(-1)*2
            scoville.append(new_scoville)
            scoville.sort()
        answer += 1
        # print(scoville)

    return answer

# print(solution([1, 2, 3, 9, 10, 12]	, 7))
print(solution([1, 2], 7))
