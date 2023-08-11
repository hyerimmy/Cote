from math import gcd

def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + num1*denum2
    num = num1*num2
    if(gcd(denum,num)!=1):
        g = gcd(denum,num)
        denum //= g
        num //= g
    answer = [denum,num]
    return answer