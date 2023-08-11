def solution(record):
    answer = []
    nick_answer = []
    nick_dict = dict()

    for r in record:
        rlist = r.split()
        if rlist[0] == "Enter":
            nick_dict[rlist[1]] = rlist[2]
            answer.append(rlist[1]+"님이 들어왔습니다.")
        elif rlist[0] == "Leave":
            answer.append(rlist[1]+"님이 나갔습니다.")
        else:
            nick_dict[rlist[1]] = rlist[2]

    for a in answer:
        nick_answer.append(a.replace(a.split("님")[0],nick_dict[a.split("님")[0]]))

    return nick_answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# ha = dict()
# print(ha)
# ha[1234]=[12]
# print(ha)
# ha[1234].append(122)
# print(ha)

# ["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.","Prodo님이 나습니다.","Prodo님이 들어왔습니다."]
# ["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.","Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]과 다릅니다.