def solution(want, number, discount):
    answer = 0
    wlist = []

    for i in range(0,len(want)):
        for _ in range(0,number[i]):
            wlist.append(want[i])
    wlist.sort()

    for k in range(0,len(discount)-9):
        if wlist == sorted(discount[k:k+10]):
            answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))