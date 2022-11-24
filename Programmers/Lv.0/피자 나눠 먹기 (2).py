from math import gcd

def solution(n):
    answer = n//gcd(6,n)
    return answer
