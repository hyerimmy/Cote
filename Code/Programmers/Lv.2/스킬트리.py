def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        index = -1
        for t in reversed(tree):
            if t in skill:
                if index-1 == skill.index(t) or index == -1:
                    index = skill.index(t)
                else:
                    index = -1
                    break
        if index == 0:
            answer += 1

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))