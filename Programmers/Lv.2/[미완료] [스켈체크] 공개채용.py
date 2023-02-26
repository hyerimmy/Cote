def solution(info, query):
    answer = []
    info_dict = []
    query_list = []
    answer_range = []

    change_anything = {1: ['cpp', 'java', 'python'],
                       2: ['backend', 'frontend'],
                       3: ['junior', 'senior'],
                       4: ['chicken', 'pizza']}

    for i in info:
        info_dict.append(i.split())
    info_dict.sort()
    print(info_dict)

    for q in query:
        query_list = ((q.replace("and", "")).split())
        print(query_list)

        for qli in range(0,len(query_list)):
            if query_list[qli] == '-':
                answer_range.append()

        # cnt = 0
        # for id in range(0,len(info_dict)):
        #     if info_dict[id][0] == query_list[0]:
        #         cnt += 1

    return answer


# print(solution(
#     ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
#      "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
#     ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
#      "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
#      "- and - and - and - 150"]))

# java 1 / python 2
print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
