

def solution(n):
    a, b = 1, 1 # a: 0개수, b: 1개수
    for i in range(2,n):
        a, b = b, a + b
    return b%1234567

print(solution(3))
print(solution(5))

def solution2(n):
    result = []
    result.append(n)

    while result[0] > 1:
        i = result[0]
        for _ in range(result.count(i)):
            result.remove(i)
            result.append(i - 1)
            result.append(i - 2)
        result.sort(reverse=True)
    return sum(result) % 1234567

def solution1(n):
    return fibo(n) % 1234567


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
