def solution(n):
    for i in range(0,n):
        if(i*i>n):
            return 2
        if(i*i==n):
            return 1