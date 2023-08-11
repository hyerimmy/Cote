print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))

def solution(my_string):
    answer = ''

    for ms in my_string:
        if ord(ms)>=97 and ord(ms)<=122:
            answer += ms.upper()
        else:
            answer += ms.lower()
    return answer

print(solution('abS'))