def solution(s):
    answer = []

    s = s[2:-2].split('},{')
    s.sort(key=len)

    for ss in s:
        ss = list(map(int, ss.split(',')))
        for ssn in ss:
            if ssn not in answer:
                answer.append(ssn)

    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
