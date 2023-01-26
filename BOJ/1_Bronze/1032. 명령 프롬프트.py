n = int(input())
result = input()
for _ in range(1,n):
    name = input()
    for i in range(0,len(result)):
        # print(result[i])
        # print(name[i])
        if result[i] != name[i]:
            if i == len(result)-1:
                result = result[:i] + "?"
            else:
                result = result[:i]+"?"+result[i+1:]


print(result)