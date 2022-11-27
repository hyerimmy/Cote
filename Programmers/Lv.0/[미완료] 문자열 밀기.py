def solution(A, B):
    answer = -1
    for num in range(1,len(A)):
        # print("-----num : ",num)
        for i in range(0,len(A)):
            # print("i : " ,i)
            # print("A[i] : " + A[i])
            # print("B[(i+1)%(len(A))] : " + B[(i+num)%(len(A))])
            if(A[i]==B[(i+num)%(len(A))]):
                answer = num
                continue
            else:
                break
        return answer

print(solution("hello","ohell"))