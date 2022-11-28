def solution(my_string):
    answer = ''.join(sorted(list(my_string.lower())))
    return answer

print(solution("Bcad"))