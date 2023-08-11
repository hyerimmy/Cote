def solution(arr1, arr2):
    answer = []
    for ar in range(0,len(arr1)):
        manswer = []
        for i in range(0,len(arr1[0])):
            manswer.append(arr1[ar][i] + arr2[ar][i])
        answer.append(manswer)
    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))