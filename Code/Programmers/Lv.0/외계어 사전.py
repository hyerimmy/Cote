def solution(spell, dic):
    spell.sort()
    for d in dic:
        if (len(d) >= len(spell)):
            d = str(sorted(list(d)))
            i = 0
            print(spell)
            print(d)
            for dd in d:
                if(spell[i] == dd):
                    i += 1
                    if(i==len(spell)):
                        return 1

    return 2


print(solution(["z", "d", "x"]	,
               ["def", "dww", "dxz", "loveaw"]	))
