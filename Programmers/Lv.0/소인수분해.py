def soinsu(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def solution(n):
    answer = []

    for i in range(2,n+1):
        if n%i == 0 and soinsu(i):
            if i not in answer:
                answer.append(i)

    return answer

print(solution(12))