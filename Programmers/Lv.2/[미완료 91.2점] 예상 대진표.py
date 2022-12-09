# 1회 우승 시 : n번(n%2) -> n//2 + n%2
# 1번(1) -> 1번
# 2번(0) -> 1번
# 3번(1) -> 2번
# 4번(0) -> 2번

def solution(n, a, b):
    answer = 0

    while 1:

        answer += 1
        a = a // 2 + a % 2
        b = b // 2 + b % 2

        if min(a, b) % 2 != 0 and (a - b) * (a - b) == 1:
            break

    return answer + 1


print(solution(8, 4, 7))
