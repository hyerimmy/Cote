def solution(n):
    print("-----",n,"-----")
    result = []
    h1 = list(range(n,0,-1))
    print(h1)
    h2 = []
    h3 = []

    if n%2 == 0:
        h2.append(h1.pop())
    else:
        h3.append(h1.pop())

    print("h1",h1)
    print("h2",h2)
    print("h3",h3)

    while h3[-1] != 0:
        if h2 == []:
            h2.append(h1.pop())
        elif h3 == []:
            h3.append(h1.pop())
        else:
            print("umm")





print(solution(2))
print(solution(3))