def solution1(ingredient):
    answer = 0
    ham = [1,2,3,1]
    h = 0

    while 1:
        for i in range(0,len(ingredient)):
            if ingredient[i] == ham[h]:
                if h == 3:
                    for _ in range(4):
                        ingredient.pop(i - 4)
                    break
                else:
                    h += 1
            else:
                h = 0
                if ingredient[i] == ham[h]:
                    h += 1
        if h == 3:
            answer += 1
            h = 0
        else:
            break

    return answer