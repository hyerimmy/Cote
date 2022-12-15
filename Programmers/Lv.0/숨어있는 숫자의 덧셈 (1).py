def solution(my_string):
    result = 0

    for ms in my_string:
        if ord(ms) >= 49 and ord(ms) <= 57:
            result += int(ms)

    return result

print(solution("aAb1B2cC34oOp"	))