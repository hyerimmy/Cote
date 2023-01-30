def solution(dirs):
    wlist = []
    pos = [0,0]
    dir = {"U":[0,1], "R":[1,0],"D":[0,-1], "L":[-1,0]}

    for d in dirs:
        way = []

        if not -5 <= pos[0] + dir.get(d)[0] <= 5:
            continue
        if not -5 <= pos[1] + dir.get(d)[1] <= 5:
            continue


        way.append([pos[0],pos[1]])
        pos[0] += dir.get(d)[0]
        pos[1] += dir.get(d)[1]

        if d == "U" or d == "R":
            way.append([pos[0],pos[1]])
        else:
            way.insert(0,[pos[0],pos[1]])

        if way not in wlist:
            wlist.append(way)

    return len(wlist)

# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
print(solution("RULRDL"))
