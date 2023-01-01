def type_is_x(str):
    if str[-1] == 'x':
        return True
    else:
        return False

def solution(polynomial):
    answer = ''
    plist = polynomial.split()

    plist[0]

    if type_is_x(plist[0]):
        xcount = int(plist[0][0:-2])
        ncount = 0
    else:
        xcount = 0
        ncount = int(plist[0])

    for i in range(1,len(plist), 2):
        if plist[i] == '+':
            if type_is_x(plist[i+1]):
                xcount += int(plist[0][0:-2])
            else:
                ncount += int(plist[0])
        else:
            if type_is_x(plist[i+1]):
                xcount *= int(plist[0][0:-2])
            else:
                ncount *= int(plist[0])


    return answer

print(solution("3x + 7 + x"	))