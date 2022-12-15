def solution(array):
    array.sort()

    answer_num = array[0]
    answer_count = 1
    num = array[0]
    count = 1

    for i in range(1,len(array)):
        if array[i] == num:
            count += 1
        else:
            num = array[i]
            count = 1

        if count == answer_count:
            answer_num = -1
        elif count > answer_count:
            answer_count = count
            answer_num = array[i]

    return answer_num

print(solution([1, 2, 3, 3, 3, 4]	))
print(solution([1, 1, 2, 2]))
print(solution([1]))

from collections import Counter
def solution1(array):
    counter = Counter(array)
    if len(array)>1 and (counter.most_common(2)[0][1]==counter.most_common(2)[1][1]):
        return -1
    else:
        return counter.most_common(1)[0][1]
