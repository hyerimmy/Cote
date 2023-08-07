def solution(number, k):
    result = ""
    if k == len(number)-1:
        return max(list(number))
    number_list = list(number)
    result_len = len(number)-k
    for i in range(1, result_len+1):
        left = result_len-i
        if left == 0:
            left = -len(number_list)
        start_number_pool = number_list[:-left]
        max_start_number = -1
        for _number in start_number_pool:
            if int(_number) > max_start_number:
                max_start_number = int(_number)
            if int(_number) == 9:
                break
        result += str(max_start_number)
        number_list = number_list[(start_number_pool.index(str(max_start_number)) + 1):]
    return result


# print(solution("1924",2))
print(solution("1331234", 3))
# print(solution("4177252841",4))
