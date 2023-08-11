import math

def solution(n):
    answer = 0
    if (sqrt := math.sqrt(n))%1==0:
        return (sqrt+1)*(sqrt+1)
    else:
        return -1

print(solution(121))