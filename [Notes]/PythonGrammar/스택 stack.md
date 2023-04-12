# 스택 stack

## python에서의 stack 구현
- 파이썬에서는 리스트로 스택을 '흉내' 낸다.

### init
```python
# 빈 스택(리스트) 초기화
stack = []
stack
```

### push
```python
stack = [1,2,3]
stack.append(4)
stack #[1,2,3,4]
```

### top
```python
stack[-1] #4
```

### pop
```python
stack.pop()
stack #[1,2,3]
```

## 참고자료
https://ooeunz.tistory.com/7