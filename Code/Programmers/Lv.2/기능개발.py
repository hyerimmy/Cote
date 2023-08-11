def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(0,len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:
            days.append((100-progresses[i]) // speeds[i] + 1)
        else:
            days.append((100-progresses[i]) // speeds[i])
    print(days)

    dcnt = 0
    dmax = days[0]

    for d in range(0,len(days)):
        print("dmax",dmax)
        print("d",days[d])
        if days[d] <= dmax:
            dcnt += 1
        else:
            answer.append(dcnt)
            dcnt = 1
            dmax = days[d]

        print("dcnt", dcnt)
        print("--")

    if dcnt != 0:
        answer.append(dcnt)

    return answer

print(solution([93, 30, 55]	,[1, 30, 5]	))