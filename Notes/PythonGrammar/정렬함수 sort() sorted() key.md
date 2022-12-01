# 정렬함수 sort() ...

## sort()
```python
>>> num_list = [15, 22, 8, 79, 10]
>>> num_list.sort()
>>> print(num_list)
[8, 10, 15, 22, 79]

>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> str_list.sort()
>>> print(str_list)
['good_morning', 'niceday', '굿모닝', '좋은하루']
```

## sorted()
```python
>>> print(sorted([15, 22, 8, 79, 10]))
[8, 10, 15, 22, 79]

>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list))
['good_morning', 'niceday', '굿모닝', '좋은하루']
```

## parameter - reverse
```python
>>> num_list = [15, 22, 8, 79, 10]
>>> num_list.sort(reverse=True)
>>> print(num_list)
[79, 22, 15, 10, 8]

>>> print(sorted(['좋은하루','good_morning','굿모닝','niceday'], reverse=True))
['좋은하루', '굿모닝', 'niceday', 'good_morning']
```

## parameter - key
```python
>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
```