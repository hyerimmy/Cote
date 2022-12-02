def solution(answers):
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    sn = [0] * 3

    for i in range(len(answers)):
        if (answers[i] == s1[i % 5]):
            sn[0] += 1
        if (answers[i] == s2[i % 8]):
            sn[1] += 1
        if (answers[i] == s3[i % 10]):
            sn[2] += 1

    maxn = max(sn)
    for i in range(len(sn)):
        if sn[i] == maxn:
            answer.append(i+1)

    return answer


print(solution([1,3,2,4,2]))
