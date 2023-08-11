def solution(num, total):
    if(num%2!=0): # n이 홀수라면
        start = total//num-(num//2)
    else: # n이 짝수라면
        start = total//num-num//2+1
    return list(range(start, start+num))
