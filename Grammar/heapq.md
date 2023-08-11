# heapq 모듈

## 1. 임포트
```python
import heapq
```

## 2. 최초 힙 생성
```python
heap = []
```

## 3. 힙에 원소 추가
heapq 모듈의 heappush() 함수를 이용하여 힙에 원소를 추가할 수 있습니다. 첫번째 인자는 원소를 추가할 대상 리스트이며 두번째 인자는 추가할 원소를 넘깁니다.
```python
heapq.heappush(heap, 4)
```

## 4. 힙에 원소 삭제
heapq 모듈의 heappop() 함수를 이용하여 힙에서 원소를 삭제할 수 있습니다. 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴합니다.
```python
heapq.heappop(heap)
```

## 5. 리스트를 힙으로 변환
이미 원소가 들어있는 리스트 힙으로 만들려면 heapq 모듈의 heapify()라는 함수에 사용하면 됩니다.
```python
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
```