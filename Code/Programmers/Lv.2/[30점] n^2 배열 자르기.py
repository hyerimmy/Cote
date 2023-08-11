# def solution(n, left, right):
#     answer = []
#     for start_number in range(1,n+1):
#         a = [start_number] * start_number
#         b = [number for number in range(start_number+1, n+1)]
#         answer.extend(a+b)
#     return answer[left:right+1]

def solution(n, left, right):
    answer = []
    start_set_idx = left//3
    end_set_idx = right//3

    print("start_set_idx",start_set_idx)

    for set_idx in range(start_set_idx, end_set_idx+1):
        start_number = set_idx + 1
        # start set
        if set_idx == start_set_idx:
            left = left % n
            print(left)
            print(start_number)
            # 1 2 3
            if (left + 1) <= start_number:
                a = [start_number] * (start_number-left)
                b = [number for number in range(start_number + 1, n + 1)]
            else:
                a = []
                b = [number for number in range(start_number + 1 + (left - start_number), n + 1)]
        # # end set
        # elif set_idx == end_set_idx:
        #     set_inner_idx = end_set_idx//n + end_set_idx%n - 1
        #     if set_inner_idx <= start_number:
        #         a = [start_number] * set_inner_idx
        #         b = []
        #     else:
        #         a = [start_number] * start_number
        #         b = [number for number in range(start_number + 1, n + 1 - (set_inner_idx - start_number))]
        # # middle set
        # else:
        #     a = [start_number] * start_number
        #     b = [number for number in range(start_number+1, n+1)]
        else:
            a = []
            b = []
        answer.extend(a+b)

    return answer

# 1 2 3 / 2 2 3 / 3 3 3

# print(solution(3,2,7))
print(solution(3,6,7))
# print(solution(4,7,14))
