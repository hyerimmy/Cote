n = int(input())
num_list = list(map(int, input().split()))
stack = []
answer = [-1] * n

for index, num in enumerate(num_list):
    while stack and num_list[stack[-1]] < num:
        answer[stack.pop()] = num
    stack.append(index)

print(' '.join([str(num) for num in answer]))