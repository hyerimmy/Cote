def solution(dots):
    answer = 0

    for i in range(1,4):
        print(i)
        di = [1,2,3]
        di.remove(i)
        a = ["a","b"]
        print(dots[i],dots[0])
        print(dots[di[0]],dots[di[1]])
        a[0] = (dots[i][0]-dots[0][0])/(dots[i][1]-dots[0][1])
        a[1] = (dots[di[0]][0]-dots[di[1]][0])/(dots[di[0]][1]-dots[di[1]][1])
        print("a[0]",a[0])
        print("a[1]",a[1])

    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]	))