def solution(cacheSize, cities):
    answer = 0
    cacheList = []

    if cacheSize == 0:
        return len(cities) * 5

    for c in cities:

        if c.lower() in cacheList:
            answer += 1
            cacheList.remove(c.lower())
        else:
            answer += 5

        if len(cacheList) == cacheSize:
            cacheList.pop()
        cacheList.insert(0, c.lower())

    return answer


# print(solution(3,
#                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3,
#                ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2,
#                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	))
# print(solution(5,
#                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	))
# print(solution(2,
#                ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0,
#                ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# print(solution(3,
#                ["Jeju", "Pangyo", "Jeju"]))

# print(solution(2, ["a", "a", "a", "b", "b", "b", "c", "c", "c"]))

print(solution(3,
               ["Jeju", "Pangyo", "Jeju", "Seoul", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
