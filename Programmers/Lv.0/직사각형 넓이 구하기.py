def solution(dots):
    answer = 0
    x = []
    y = []
    for d in dots:
        if d[0] not in x:
            x.append(d[0])
        if d[1] not in y:
            y.append(d[1])

    x.sort()
    y.sort()

    answer = (x[1]-x[0]) * (y[1]-y[0])
    return answer