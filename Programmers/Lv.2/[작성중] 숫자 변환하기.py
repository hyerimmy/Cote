def calculate(x_dict, y, n) -> dict:
    result = dict()
    for x, cnt in x_dict.items():
        for new_x in [x*3, x*2, x+n]:
            if new_x <= y:
                result[new_x] = cnt+1
    return result


def solution(x, y, n):
    a = calculate({x: 0}, y, n)
    return calculate(a, y, n)
    # answer = 0
    #
    # return answer

print(solution(10, 40, 5))