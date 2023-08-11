# Deep Copy
https://wikidocs.net/16038

## 깊은 복사
깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것입니다.
copy.deepcopy메소드가 해결해줍니다.
```python
>>> import copy
>>> a = [[1,2],[3,4]]
>>> b = copy.deepcopy(a)
>>> a[1].append(5)
>>> a
[[1, 2], [3, 4, 5]]
>>> b
[[1, 2], [3, 4]]
```