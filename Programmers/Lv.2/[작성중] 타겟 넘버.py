def sum_lastnum(nlist, rlist):
    for i in range(0,len(nlist)):
        rlist[0] += nlist[i][-1]
        nlist[i].pop()

def solution(numbers, target):
    answer = 0

    nlist = []
    nlist.append(numbers)
    rlist = []
    rlist.append(0)

    while len(nlist[0]) != 0:
        sum_lastnum(nlist, rlist)
        print(nlist)
        print(rlist)
        print("----")

    return answer

print(solution([4, 1, 2, 1]	))