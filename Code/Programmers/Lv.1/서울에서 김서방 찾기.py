def solution(seoul):
    answer = ''
    for i in range(0,len(seoul)):
        if seoul[i] == 'Kim':
            return "김서방은 "+str(i)+"에 있다"
    return answer

print(solution(["Jane", "Kim"]))