def solution(numbers):
    answer = 0
    number_set = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
                  "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    str = ''
    for n in numbers:
        str += n
        if str in number_set:
            answer = answer*10 + int(number_set.get(str))
            str = ''

    return answer

print(solution("onetwothreefourfivesixseveneightnine"	))
print(solution("zeroonetwothreefourfivesixseveneightnine"	))
