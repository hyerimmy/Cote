# deque
## 앞뒤에서 자료를 넣고 빼려면?
**collections.deque**
- deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형으로, 스택(stack)처럼 써도 되고 큐(queue)처럼 써도 된다. collections.deque 모듈은 deque 자료형을 생성하는 모듈이다.
- deque는 '데크'라 읽는다.

*tip : list.pop(-1)보다 deque 활용하는 것이 시간복잡도를 줄이는 방법!!
```python
>>> from collections import deque
>>> d = deque([1,2,3,4,5])
>>> d.append(6)
>>> d
deque([1, 2, 3, 4, 5, 6])
>>> d.appendleft(0)
>>> d
deque([0, 1, 2, 3, 4, 5, 6])
>>> d.pop()
6
>>> d
deque([0, 1, 2, 3, 4, 5])
>>> d.popleft()
0
>>> d
deque([1, 2, 3, 4, 5])
>>>
```

리스트를 n만큼 회전하는 문제는 알고리즘 문제에서 자주 등장한다. 파이썬에서는 collections.deque 모듈을 사용하면 간단하게 이 문제를 해결할 수 있다.
```python
>>> from collections import deque
>>> a = [1, 2, 3, 4, 5]
>>> q = deque(a)
>>> q.rotate(2)  #시계방향 회전은 양수, 그 반대는 음수
>>> result = list(q)
>>> result
[4, 5, 1, 2, 3]
```
