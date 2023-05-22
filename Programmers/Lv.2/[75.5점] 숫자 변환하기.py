def calculate(y_list, x, n, cnt):
    new_y_list = []
    for y in y_list:
        for new_y in [y/3, y/2, y-n]:
            if new_y == x:
                return True, cnt+1
            elif new_y > x and (new_y == int(new_y)):
                new_y_list.append(new_y)
    return False, new_y_list

def solution(x, y, n):
    if x == y:
        return 0
    is_find = False
    cnt = 0
    result = [y]
    while not is_find:
        is_find, result = calculate(result, x, n, cnt)
        cnt+=1
        if is_find:
            return result
        if not is_find and not result:
            return -1

print(solution(10, 40, 5))
print(solution(2, 5, 4))
print(solution(10, 40, 30))
