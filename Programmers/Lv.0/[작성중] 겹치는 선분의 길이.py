def solution(lines):
    answer = 0
    nlines = []
    alines = []

    for l in lines:
        print("------")
        print(l)
        for li in range(l[0],l[1]+1):
            if li in nlines and li not in alines:
                alines.append(li)
            nlines.append(li)

    print(nlines)
    print(alines)
    return len(alines)

print(solution([[0, 1], [2, 5], [3, 9]]	))