def solution(rsp):
    answer = ''
    win = {'0':'5', '2':'0', '5':'2'}

    for r in rsp:
        answer += win.get(r)

    return answer

print(solution('2'))
print(solution('205'))