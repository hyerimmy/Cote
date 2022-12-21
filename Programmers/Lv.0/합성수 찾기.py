def findhap(n):
    for i in range(2,n-1):
        if n%i == 0:
            return True
    return False

def solution(n):
    answer = 0
    for nn in range(1,n+1):
        if findhap(nn):
            answer += 1
    return answer

