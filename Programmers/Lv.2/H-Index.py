def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    for i in range(0,len(citations)):
        if citations[i] >= i+1:
            answer = i+1

    return answer

print(solution([3, 0, 6, 1, 5]	))


# 1 2 3 4 5
