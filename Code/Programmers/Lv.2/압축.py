def solution(msg):
    answer = []

    word_dict = dict()
    for index in range(1,27):
        word_dict[chr(index+64)] = index

    while msg:
        i = 1
        index = None
        while not index:
            if msg[0:i] in word_dict:
                if msg[0:i] == msg:
                    index = word_dict.get(msg[0:i])
                    msg = None
                    break
                i += 1
            else:
                word_dict[msg[0:i]] = len(word_dict)+1
                index = word_dict.get(msg[0:i - 1])
                msg = msg[i - 1:]
        answer.append(index)

    return answer

# print(solution("KAKAO"))

# print(solution("TOBEORNOTTOBEORTOBEORNOT"))

print(solution("ABABABABABABABAB"))