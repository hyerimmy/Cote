def solution(before, after):

    blist = sorted(list(before))
    alist = sorted(list(after))

    return int(alist == blist)

print(solution("abc","cba"))