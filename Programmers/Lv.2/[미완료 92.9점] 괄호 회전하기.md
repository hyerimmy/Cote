def solution(s):
    answer = 0
    pair = {"(": ")", "[": "]", "{": "}"}

    for i in range(0, len(s)):
        answer += 1
        ss = s[i:] + s[:i]
        shistory = []
        for ssi in range(0, len(ss)):
            if ss[ssi] in pair:
                shistory.append(ss[ssi])
            else:
                if not shistory:
                    answer -= 1
                    break
                if pair[shistory[-1]] == ss[ssi]:
                    shistory.pop()
                else:
                    answer -= 1
                    break

    return answer


# print(solution("[](){}"))
# print(solution("12345"))

print(solution("}]()[{"))

# print("**")
# shis = ['(','}']
# print(shis)
# print(shis[-1])

# print("**************")
# pair = {"(": ")"}
# print(pair)
# if "(" in pair:
#     print('if "(" in pair:')
#
#
# if ")" in pair:
#     print('if ")" in pair:')
# print(pair["("])

