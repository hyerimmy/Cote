def cal_num(n, rlist):
    new_rlist = []
    for rl in rlist:
        new_rlist.append(rl+n)
        new_rlist.append(rl-n)
    return new_rlist

def solution(numbers, target):
    answer = 0
    rlist = [numbers[0], -numbers[0]]

    for i in range(1,len(numbers)):
        rlist = cal_num(numbers[i],rlist)

    for rl in rlist:
        if rl == target:
            answer += 1

    return answer

print(solution([1,1,1, 1,1],3))
# print(solution([4, 1, 2, 1],4))
