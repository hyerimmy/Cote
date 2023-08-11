def move(loc, n, m):
    new_loc = []
    direction = [[0,1],[0,1]]

    for i in range(0,1):
        loc_x = loc[0] + direction[i][0]
        loc_y = loc[1] + direction[i][1]
        if loc_x <=n and loc_y <= m:
            new_loc.append([loc_x,loc_y])
    return new_loc


def solution(maps):
    answer = 0
    loc = [1,1]
    n = len(maps[0])
    m = len(maps)

    loc_list = []
    cnt_list = []

    while loc_list[-1] != [n,m]:
        loc_list = move(loc,n,m)



    return answer