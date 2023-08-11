from itertools import permutations

def solution(expression):
    expression_list = []
    start_idx = 0
    for idx, letter in enumerate(expression):
        if letter in ["*","-","+","/"]:
            expression_list.append(expression[start_idx:idx])
            expression_list.append(letter)
            start_idx = idx+1
    expression_list.append(expression[start_idx:])
    operator_list = [operator for operator in ["*","-","+","/"] if operator in expression_list]
    permutations_list = list(permutations(operator_list))

    answer = 0

    for permutation in permutations_list:
        # print("-")
        # print(permutation)
        expression = expression_list
        for operator in permutation:
            for _ in range(expression.copy().count(operator)):
                idx = expression.index(operator)
                if operator == "*":
                    result = int(expression[idx - 1]) * int(expression[idx + 1])
                elif operator == "+":
                    result = int(expression[idx - 1]) + int(expression[idx + 1])
                elif operator == "-":
                    result = int(expression[idx - 1]) - int(expression[idx + 1])
                expression = expression[:idx - 1] + [result] + expression[idx + 2:]
                # print(expression)
        expression_result = expression.pop()
        if expression_result < 0:
            expression_result *= -1
        if expression_result > answer:
            answer = expression_result

    return answer

print(solution("50*6-3*2"))
print(solution("100-200*300-500+20"))
