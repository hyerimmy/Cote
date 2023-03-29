def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def solution(n, k):
    answer = []
    nlist = list(range(1, n+1))

    for _ in range(0,n):
        sub = factorial(n-1)
        if k == sub:
            answer = answer + nlist
            break
        if k == 0:
            answer.append(nlist.pop(k//sub -1))
        answer.append(nlist.pop(k // sub))
        new = [k // n, k % n]
        k = new[0]
        n = new[1]

    return answer

print(solution(3,5))