def solution(clothes):

    result = 1
    ctype = []

    for c in clothes:
        if c[1] not in ctype:
            ctype.append(c[1])
            globals()[c[1]] = list()
        globals()[c[1]].append(c[0])

        print(globals()[c[1]])

    for ct in ctype:
        result  *= len(globals()[ct])

    if len(ctype) != 1:
        result += len(clothes)
    return result


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellow_hat", "headgear"]]))

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgearr"]]))