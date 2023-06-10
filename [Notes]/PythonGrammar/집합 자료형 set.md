# 집합 자료형 set
set() 은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.
집합 자료형은 다음과 같이 set 키워드 를 사용해 만들 수 있다.

## set()의 특징
- 중복을 허용하지 않는다.
- 순서가 없다.
리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만,
set 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.

만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트 or 튜플로 변환한 후 해야 한다.
```python
s1 = set([1,2,3])

l1 = list(s1)
print(l1)		# result : [1,2,3]
print(l1[0])		# result : 1

t1 = tuple(s1)
print(t1)		# result : (1,2,3)
print(t1[0])		# result : 1
```

### 1) 값 1개 추가히기(add)
이미 만들어진 set 자료형에 값을 추가할 수 있다.
```python
s1 = set([1,2,3])
s1.add(4)
print(s1)	#result : {1, 2, 3, 4}
```
2) 값 여러개 추가하기(update)
```python
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)	#result : {1, 2, 3, 4, 5, 6}
```
3) 특정 값 제거하기(remove)
```python
s1 = set([1,2,3])
s1.remove(2)
print(s1)	#result : {1, 3}
```