import math

def solution(arr):

    for num in range(max(arr), math.prod(arr)):
        for i in range(0,len(arr)):
            if num % arr[i] == 0:
                if i == len(arr)-1:
                    return num
                else:
                    continue
            else:
                break

    return math.prod(arr)


print(solution([2, 7]))
print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
