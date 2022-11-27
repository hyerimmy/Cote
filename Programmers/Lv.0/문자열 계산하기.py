def solution(my_string):
    mslist = my_string.split()
    answer = int(mslist[0])
    for i in range(1,len(mslist),2):
        if(mslist[i]=="+"):
            answer += int(mslist[i+1])
        elif(mslist[i]=="-"):
            answer -= int(mslist[i+1])
    return answer

print(solution("3 + 5"))