def calculate(x_list, y, n, cnt):
    new_x_list = []
    for x in x_list:
        for new_x in [x*3, x*2, x+n]:
            if new_x == y:
                return True, cnt+1
            elif new_x < y:
                new_x_list.append(new_x)
    return False, new_x_list

def solution(x, y, n):
    is_find = False
    cnt = 0
    result = [x]
    while not is_find:
        is_find, result = calculate(result, y, n, cnt)
        cnt+=1
        if is_find:
            return result
        if not is_find and not result:
            return -1

print(solution(10, 40, 5))
print(solution(2, 5, 4))
print(solution(10, 40, 30))
