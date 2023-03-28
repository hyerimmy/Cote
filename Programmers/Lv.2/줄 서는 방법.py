def solution(n, k):
    answer = []
    nlist = list(range(1, n+1))

    while n != 1:
        sub = 1
        for i in range(1, n):
            sub *= i
        if k == sub:
            for n in nlist:
                answer.append(n)
            break
        answer.append(nlist.pop(k // sub))
        new = [k // n, k % n]
        k = new[0]
        n = new[1]

    return answer

print(solution(3,5))