def solution(A,B):
    answer = -1
    for num in range(0,len(A)):
        if(A[len(A) - num:len(A)]+A[0:len(A) - num] == B):
            answer = num
    return answer