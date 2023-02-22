def get_result(arr1, arr2, a, b, k):
    result = 0
    for i in range(0,k):
        result += arr1[a][i]*arr2[i][b]
    return result

def solution(arr1, arr2):
    answer = []

    if len(arr1[0]) != len(arr2):
        arr_temp = arr1
        arr1 = arr2
        arr2 = arr_temp

    k = len(arr1[0])

    for a in range(0,len(arr1)):
        aa = []
        for b in range(0,len(arr2[0])):
            aa.append(get_result(arr1, arr2, a, b, k))
        answer.append(aa)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]]	,[[3, 3], [3, 3]]	))
# print(get_result([[1, 4], [3, 2], [4, 1]]	,[[3, 3], [3, 3]],0,1,2))