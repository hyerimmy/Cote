import math

def solution(a, b):
    while math.gcd(a,b) > 1:
        gcd_num = math.gcd(a,b)
        a //= gcd_num
        b //= gcd_num

    while b%2==0:
        b /= 2

    while b%5==0:
        b /= 5

    return 1 if b==1 else 2

print(solution(7,20))
print(solution(11,22))
print(solution(12,21))
