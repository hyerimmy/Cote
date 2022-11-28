def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        new_str = ""
        for k in range(0,n):
            if ((i+k) > len(my_str)-1):
                break
            new_str += my_str[i+k]
        answer.append(new_str)
    return answer

print(solution("abc1Addfggg4556b",6))
