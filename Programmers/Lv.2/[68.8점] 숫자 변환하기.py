def calculate(x_list, y, n, cnt):
    new_x_list = []
    for x in x_list:
        for new_x in [x*3, x*2, x+n]:
            if new_x == y:
                return cnt
            elif new_x < y:
                new_x_list.append(new_x)
    if new_x_list:
        return calculate(new_x_list, y, n, cnt+1)
    else:
        return -1

def solution(x, y, n):
    cnt = calculate([x], y, n, 1)
    return cnt

# print(solution(10, 40, 5))
print(solution(2, 5, 4))
