def solution(n, numlist):
    for nl in numlist:
        if(nl%n!=0):
            numlist.remove(nl)
    # answer = []
    return numlist