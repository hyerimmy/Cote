# - y = (width - 2)x(height - 2)
# - b = 전체면적 - y


def solution(brown, yellow):
    answer = []
    for height in range(3, yellow + 3):
        if yellow % (height -2) == 0:
            width = yellow // (height - 2) + 2
            if (height * width - yellow) == brown:
                answer = [height, width]
                answer.sort(reverse=True)
                break
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))