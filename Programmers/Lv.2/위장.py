def solution(clothes):
    result = 1
    cnthash = {}

    for c in clothes:
        if c[1] in cnthash.keys():
            cnthash[c[1]] += 1
        else:
            cnthash[c[1]] = 1

    for chv in cnthash.values():
        result *= (chv + 1)

    return result-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellow_hat", "headgear"]]))
#
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgearr"]]))

# c = {}
# c['a']=15
# print(c)
# print(c['a'])
# c['b']=15
# print(c)
# print(c['b'])
# print(c.keys())
# if c['b']:
#     print(c['b'])
