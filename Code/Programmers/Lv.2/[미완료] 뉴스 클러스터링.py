def sep_str(str):
    slist = []
    for i in range(0, len(str) - 1):
        s1 = str[i].lower()
        s2 = str[i + 1].lower()
        if 97 <= ord(s1) <= 122 and 97 <= ord(s2) <= 122:
            slist.append(s1 + s2)
    return slist

def count_str(slist):
    clist = {}
    for sl in slist:
        if sl not in clist:
            clist[sl] = 1
        else:
            clist[sl] += 1
    return clist

def solution(str1, str2):
    answer = 0

    slist1 = sep_str(str1)
    slist2 = sep_str(str2)

    print(slist1)
    print(slist2)

    clist1 = count_str(slist1)
    clist2 = count_str(slist2)

    print(clist1)
    print(clist2)


    return answer

print(solution('FRANCE','french'))
print(solution('aa1+aa2','AAAA12'))