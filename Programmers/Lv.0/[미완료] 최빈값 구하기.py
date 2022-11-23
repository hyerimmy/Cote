from collections import Counter

def solution(array):
    counter = Counter(array)
    if len(array)>1 and (counter.most_common(2)[0][1]==counter.most_common(2)[1][1]):
        return -1
    else:
        return counter.most_common(1)[0][1]


print(solution([1, 2, 3, 3, 3, 4]))

print(Counter([1, 2, 3, 3, 3, 4]).most_common())
print(Counter([1, 2, 3, 3, 3, 4]).most_common(2))
print(Counter([1, 2, 3, 3, 3, 4]).most_common(2)[0])
print(Counter([1, 2, 3, 3, 3, 4]).most_common(2)[1])