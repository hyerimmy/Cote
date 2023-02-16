def solution(s):
    answer = True

    pn = 0
    yn = 0

    for ss in s:
        if ss.upper() == "P":
            pn += 1
        elif ss.upper() == "Y":
            yn += 1

    return pn==yn

print(solution("pPoooyY"))