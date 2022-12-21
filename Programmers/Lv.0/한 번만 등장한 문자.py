def solution(s):
    answer = []
    not_answer = []

    slist = list(s)

    for sl in slist:
        if sl not in answer and sl not in not_answer:
            answer.append(sl)
        else:
            if sl in answer:
                answer.remove(sl)
            if sl not in not_answer:
                not_answer.append(sl)

        answer.sort()

        result = ''
        for a in answer:
            result += a

    return result


from collections import Counter


def solution1(s):
    counter = Counter(s)
    print(counter)
    print(list(counter))
    answer = ''
    return answer


print(solution("abcabcadc"))
