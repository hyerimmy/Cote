# 람다식 lambda

## 1. 람다(lambda)
1 ) 의미 익명함수를 지칭하는 용어 즉, 기존의 함수(명 등)을 선언하고
사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수.

2 ) 형식 : lambda 인자 : 표현식 예시) sum = lambda x: x+1

3 ) 인자 넣기 : 람다 표현식을 괄호로 묶은 뒤에 다시 괄호를 붙이고 인수를 넣어 호출

```python
(lambda x: x + 10)(1) 
> 11
```
4 ) 인자 두 개 쓰기 : lambda x,y: x+y 

5 ) if 사용하기
```python
check_pass = lambda x: 'pass' if x>=70 else 'fail'
```
## 2. 리스트를 정렬 key 사용(sort, sorted)
a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
 

▷ key 인자를 정하지 않은 기본적인 sort에선, 튜플 순서대로 우선순위 기본 할당
```python
# 앞의 인자로 정렬됨
b = sorted(a)
b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
```

▷ key 인자에 함수를 넘겨주면 우선순위가 정해짐.
```python
c = sorted(a, key = lambda x : x[0]) 

c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1]) 

d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]
```

▷ 비교할 아이템이 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.

▷ -를 붙이면, 현재와 반대차순으로 정렬된다.
```python
e = sorted(a, key = lambda x : (x[0], -x[1])) 
=> [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

f = sorted(a, key = lambda x : -x[0]) 
=> [(5, 1), (5, 2), (3, 0), (1, 2), (0, 1)])
```

▷ 뒤에 문자 순 정렬
```python
s = ['2 A', '1 B', '4 C', '1 A']
s.sorted(s, key=lambda x: (x.split()[1], x.split()[0]))
=> ['1 A', '2 A', '1 B', '4 C']
```
```python
a_list = ['a', 'b', 'd', 'd', 'b','s']
a_counter = Counter(a_list).most_common()
=> [('b', 2), ('d', 2), ('a', 1), ('s', 1)]

# 문자 역순(아스키 값 이용)
sorted(a_counter,  key=lambda x: (-x[1], -ord(x[0])))
=> [('d', 2), ('b', 2), ('s', 1), ('a', 1)]
```

## 3. map 람다 표현식
▷ list(map(lambda x: x , list ) 표현식
```python
list(map(lambda x: x+10, [1,2,3]))

=> [11, 12, 13]
```

## 4. filter()
조건식의 boolean 값이 True 참인 요소만 반환한다.
```python
a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]

result = list(filter(lambda x : x > 7 and x < 15, a))

=> [8, 9, 11, 13]
```

## 5. reduce() 표현식
reduce() 는 값을 누적시킨다. 

( reduce는 functools 모듈을 불러와야 사용가능 )
```python
 from functools import reduce t = [47, 11, 42, 13]

 result = reduce(lambda x, y : x + y, t)

=> 113
```