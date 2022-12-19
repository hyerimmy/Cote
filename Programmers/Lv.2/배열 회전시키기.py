def solution(numbers, direction):
    answer = []

    if direction == 'right':
        dnum = -1
    else:
        dnum = 1

    for i in range(0,len(numbers)):
        answer.append(numbers[(i+dnum)%len(numbers)])

    return answer

print(solution([1, 2, 3],'right'))
print(solution([1, 2, 3],'left'))