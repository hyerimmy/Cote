def solution(arr1, arr2):
    answer = [[]]

    for k in range(0,len(arr1)):
        for i in range(0,len(arr2)):
            print("arr1[k][i]",arr1[k][i])
            print("arr2[i][k]",arr2[i][k])
            print("--------")

    # for a1 in arr1:
    #     for i in range(0, len(arr2)):
    #         for a2 in arr2:
    #             for k in range(0, len(arr2)):
    #                 print("a1[k]", a1[k])
    #                 print("a2[k]", a2[k])
    #                 print("a1[k]*a2[k]", a1[k] * a2[k])

    print()

    for i in range(0, len(arr2)):
        for a2 in arr2:
            print(a2[i])

    return answer


print(solution([[1, 4], [3, 2], [4, 1]],
               [[1, 2], [3, 4]]))
