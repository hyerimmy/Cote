# 타임에러
def solution1(str1, str2):
    for i in range(0,len(str1)):
        if(str1[i]==str2[0]):
            answer = 1
            for k in range(0,len(str2)):
                if(str1[i+k]!=str2[k]):
                    answer = 2
                    break
    return answer

def solution(str1, str2):
    k = 0
    for i in range(0,len(str1)):
        if (str1[i] == str2[k]):
                k+=1
                if(k==len(str2)):
                    return 1
        else:
            k=0
    return 2

print(solution("ab6CDE443fgh22iJKlmn1o"	,"6CD"	))