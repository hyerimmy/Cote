def solution(babbling):
    answer = 0
    sound = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for s in sound:
            b = b.replace(s,"-")
            if b.replace("-","") == "":
                answer += 1
                break

    return answer

print(solution(["aya","ayaye","wosoayaaya"]))
print(solution(["aya", "yee", "u", "maa", "wyeoo"]	))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	))