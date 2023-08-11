def solution(my_string, num1, num2):

    return \
        my_string[0:num1]+ \
        my_string[num2]+ \
        my_string[num1+1:num2]+ \
        my_string[num1]+ \
        my_string[num2 + 1:]

# print(solution("hello",1,2))
print(solution("01234567"	,3,6))