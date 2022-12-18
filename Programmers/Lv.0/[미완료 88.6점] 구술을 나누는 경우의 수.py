from itertools import combinations

def solution(balls, share):
    answer = len(list(
        combinations(list(range(balls)), share)))

    return answer

print(solution(3,2))
print(solution(5,3))