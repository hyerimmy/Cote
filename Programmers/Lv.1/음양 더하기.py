def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(absolutes)):
        if(signs[i] == true):
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer