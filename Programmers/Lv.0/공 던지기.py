def solution(numbers, k):

    kk = 1
    result = 1

    while kk < k:
        result = (result+2) % len(numbers)
        kk += 1


    return result

print(solution([1, 2, 3, 4],2))