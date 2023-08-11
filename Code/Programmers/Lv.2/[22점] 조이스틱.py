def solution(name):
    answer = 0
    name_list = list(name)
    answer += (ord(name_list.pop(0)) - 65)

    for cnt in range(0,len(name_list)):
        if name_list[0+cnt] == "A" and name_list[-1-cnt] != "A":
            name_list = name_list[cnt+1:]
            break
        if name_list[0+cnt] != "A" and name_list[-1-cnt] == "A":
            name_list = name_list[:cnt]
            answer += 1
            break

    for alphabet in name_list:
        answer += 1
        moving_cnt = min(ord(alphabet)-ord("A"), ord("Z")-ord(alphabet)+1)
        answer += moving_cnt

    return answer


print(solution("JEROEN"))
print(solution("JAN"))