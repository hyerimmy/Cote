def solution(topping):
    answer = 0

    end_topping_dict = dict()
    start_topping_dict = dict()
    for topping_type in set(topping):
        end_topping_dict[topping_type] = topping.count(topping_type)

    for topping in topping:
        if end_topping_dict[topping] > 1:
            end_topping_dict[topping] -= 1
        else:
            end_topping_dict.pop(topping)

        if topping in start_topping_dict:
            start_topping_dict[topping] += 1
        else:
            start_topping_dict[topping] = 1

        if len(start_topping_dict) == len(end_topping_dict):
            answer += 1
    return answer

print(solution(	[1, 2, 1, 3, 1, 4, 1, 2]))
