def solution(x):
    target_num = sum(list(map(int, list(str(x)))))
    return x % target_num == 0


print(solution(12))