# OX퀴즈

https://school.programmers.co.kr/learn/courses/30/lessons/120907

### 문제 설명
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

### 코드
```python
def solution(quiz):
    answer = []

    for q in quiz:
        qq = q.split()

        if qq[1] == '+':
            ans = int(qq[0]) + int(qq[2])
        elif qq[1] == '-':
            ans = int(qq[0]) - int(qq[2])

        if int(qq[4]) == ans:
            answer.append("O")
        else:
            answer.append("X")

    return answer
```