def solution(bin1, bin2):
    return format(int(bin1,2) + int(bin2,2),'b')

print(solution("10","11"))