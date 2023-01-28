# 딕셔너리 자료형

## 딕셔너리란?
요즘 사용하는 대부분의 언어 **대응 관계를 나타내는 자료형**을 갖고 있는데,
이를 연관 배열(Associative array) 또는 **해시(Hash)**라고 한다.
```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
>>> dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
```

## 빈 딕셔너리 생성
```python
s = dict()
```

## 딕셔너리 쌍 추가, 삭제
```python
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}
```

## 딕셔너리 요소 삭제
```python
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
```

## 딕셔너리 key 사용해 value 얻기
```python
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99

>>> a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'010-9999-1234'
```

## 관련 함수들
```python
>>> a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])

>>> list(a.keys())
['name', 'phone', 'birth']

>>> a.values()
dict_values(['pey', '010-9999-1234', '1118'])
```

### 참고자료
https://wikidocs.net/16