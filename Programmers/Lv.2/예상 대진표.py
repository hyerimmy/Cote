# 1회 우승 시 : n번(n%2) -> n//2 + n%2
# 1번(1) -> 1번
# 2번(0) -> 1번
# 3번(1) -> 2번
# 4번(0) -> 2번

import math

def solution(n, a, b):
    answer = 1

    if min(a, b) % 2 != 0 and (a - b) * (a - b) == 1:
        return answer

    for ni in range(0,n):
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)

        if min(a, b) % 2 != 0 and (a - b) * (a - b) == 1:
            break

    return answer


print(solution(8, 4, 7))

