def solution(N, road, K):
    answer = 0

    road_dict = dict()
    for i in range(1,N+1):
        road_dict[i] = dict()

    for road_data in road:
        print(road_data)
        road_dict[road_data[0]][road_data[1]] = road_data[2]
        road_dict[road_data[1]][road_data[0]] = road_data[2]
    print(road_dict)

    def go_one_road(history: dict, destination: int):
        for route in history.copy():
            history.pop(route)
            current = route[-1]
            for key, value in road_dict[current].items():
                pass


    for destination in range(2,N+1):
        print(destination)
        result_list = []
        road_dict[]
        go_one_road(0,[1],1,destination,[])

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))