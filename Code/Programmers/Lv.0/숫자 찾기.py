def solution(num, k):
    for i in range(0,len(str(num))):
        if(str(num)[i]==str(k)):
            return i+1
    return -1
