def solution(n, numlist):
    answer = []
    for nl in numlist:
        if(nl%n==0):
            answer.append(nl)
    return answer