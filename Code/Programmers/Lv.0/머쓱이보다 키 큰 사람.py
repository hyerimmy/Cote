def solution(array, height):
    answer = 0
    for a in array:
        if(a>height):
            answer += 1
    return answer

print(solution([149, 180, 192, 170], 167))