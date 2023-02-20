def solution(bridge_length, weight, truck_weights):
    answer = 0

    t0 = truck_weights
    t1 = []
    t2 = []

    print("truck_weights",truck_weights)
    print("t0",t0)

    while t0 is not []:
        answer+=1
        t0.pop()
        print(t0)

    return answer

print(solution(2,10,[7,4,5,6]))