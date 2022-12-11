def solution(n):
    ans = 0

    while n>0:
        if n%2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1

    return ans

print(solution(5))
print(solution(6))
print(solution(5000))