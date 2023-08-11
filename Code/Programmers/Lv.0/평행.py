def solution(dots):
    answer = 0

    for i in range(1,4):
        di = [1,2,3]
        di.remove(i)
        a = ["a","b"]
        a[0] = (dots[i][1]-dots[0][1])/(dots[i][0]-dots[0][0])
        a[1] = (dots[di[0]][1]-dots[di[1]][1])/(dots[di[0]][0]-dots[di[1]][0])
        if a[0] == a[1]:
            return 1

    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]	))