def solution(phone_number):
    answer = ''
    for i in range(0,len(phone_number)):
        if i in range(len(phone_number)-4,len(phone_number)):
            answer += phone_number[i]
        else:
            answer += '*'
    return answer

print(solution("01033334444"))