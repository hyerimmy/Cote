def solution(number, k):
    for _ in range(0,k):
        start_number_pool = list(number)[0:k+1]
        max_start_number = max(list(number)[0:k+1])
        print(max_start_number)
        new_number_list = ["".join(number[index:]) for index, value in enumerate(start_number_pool) if max_start_number==value]
        print(new_number_list)
        if len(new_number_list) == 1:
            break
        else:
            k += 1
    # print(start_number_pool)
    # print(max_start_number)
    # print(index_list)
    # while len(index_list) > 1:
    #     print(start_number_pool)
    #     print(max_start_number)
    #     print(index_list)
    #     start_number_pool = [index+1 for index in index_list]
    #     max_start_number = max(start_number_pool)
    #     index_list = [index for index, value in enumerate(start_number_pool) if max_start_number==value]

    answer = ''
    return answer

# print(solution("1924",2))
# print(solution("1231234",3))
print(solution("4177252841",4))
