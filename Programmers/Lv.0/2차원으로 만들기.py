def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        num_set = []
        for k in range(0,n):
            num_set.append(num_list[i+k])
        answer.append(num_set)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8]	,2))