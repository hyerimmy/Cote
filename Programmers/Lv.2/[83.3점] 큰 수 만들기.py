def solution(number, k):
    result = ""
    number_list = list(number)
    result_len = len(number)-k
    for i in range(1, result_len+1):
        left = result_len-i
        print("left - ", left)
        if left == 0:
            left = -len(number_list)
        start_number_pool = number_list[:-left]
        print("number_list-> ",number_list)
        print("start-> ",start_number_pool)
        max_start_number = max(start_number_pool)
        result += str(max_start_number)
        print("--result",result)
        number_list = number_list[(start_number_pool.index(max_start_number) + 1):]
    return result

# print(solution("1924",2))
print(solution("1231234",3))
# print(solution("4177252841",4))
