def solution(array):
    bignum = sorted(array)[-1]
    for i in range (0,len(array)):
        if(array[i]==bignum):
            answer = [sorted(array)[-1], i]
    return answer