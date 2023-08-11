def solution(s):
    stack = []
    for ss in s:
        if ss == '(':
            stack.append(ss)
        elif ss == ')':
            if stack == []:
                return False
            else:
                stack.pop()

    return stack == []

print(solution("()()"))
print(solution("()(()"))
print(solution("()()()()"))