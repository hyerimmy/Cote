def solution(arr):
    min = sorted(arr)[0]
    if len(arr) == 1 or arr[0]==arr[1]:
        arr = [-1]
    else:
        arr.pop(arr.index(min))
    return arr

print(solution([4,3,2,1]))
print(solution([10]))
