def solution(polynomial):
    npol = polynomial.split(" ")
    xcnt = 0
    ncnt = 0

    for i in range(0,len(npol),2):
        if npol[i][-1] == 'x':
            if npol[i] == 'x':
                xcnt += 1
            else:
                xcnt += int(npol[i][0:-1])
        else:
            ncnt += int(npol[i])

    if xcnt == 0:
        answer = str(ncnt)
    elif ncnt == 0:
        if xcnt == 1:
            answer = 'x'
        else:
            answer = str(xcnt) + 'x'
    else:
        if xcnt == 1:
            answer = 'x' + ' + ' + str(ncnt)
        else:
            answer = str(xcnt)+'x'+' + '+str(ncnt)

    return answer

print(solution("3 + 7 + x"))
print(solution("x"))