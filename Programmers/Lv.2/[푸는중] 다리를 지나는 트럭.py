def solution(bridge_length, weight, truck_weights):
    answer = 0

    t0 = truck_weights
    t1 = []
    t2 = []
    t1_togo = []

    # print("truck_weights", truck_weights)
    # print("t0", t0)

    while len(t0) > 0 or len(t1) > 0:
        answer += 1

        try:
            if t1_togo[0] > bridge_length:
                t2.append(t1.pop(0))
                t1_togo.pop(0)
        except IndexError:
            pass

        if len(t1) <= bridge_length and len(t0) > 0:
            if sum(t1) + t0[0] <= weight:
                t1.append(t0.pop(0))
                t1_togo.append(0)

        for i in range(0, len(t1_togo)):
            t1_togo[i] += 1


        print("--------")
        print("<answer> = ", answer)
        print("t0", t0)
        print("t1", t1)
        print("t1_togo", t1_togo)
        print("t2", t2)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
