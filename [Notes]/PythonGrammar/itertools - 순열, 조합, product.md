# itertools - 순열, 조합, product

## Python itertools
파이썬으로 코딩할 때, 종종 순열, 조합, product를 구현하거나 사용해야 할 때가 있다. 이럴 때 힘들게 구현하지 말고 파이썬에서 만들어둔 표준 라이브러리인 itertools를 사용해보자

## 조합 combinations
조합을 표현할 때 사용되는 메소드이다. 한 리스트에서 중복을 허용하지 않고 모든 경우의 수를 구하는 것이다. 반환되는 항목의 수는 n! / r! / (n - r)!이다. 사용법은 다음과 같다.

## 순열 permutations
순열을 표현할 때 사용되는 메소드이다. 한 리스트에서 중복을 허용하고 모든 경우의 수를 구하는 것이다. 반환되는 항목의 수는 n! / r!이다.

```
    dataset = ['A', 'B', 'C']

    printList = list(permutations(dataset, 2))
    print(printList)
    
    # 결과값
    # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    dataset = ['A', 'B', 'C']

    printList = list(permutations(dataset, 3))
    print(printList)
    
    # 결과값
    # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```
## 데카르트곱 product (모든조합)
데카르트 곱이라고도 하는 cartesian product를 표현할 때 사용하는 메소드이다(DB의 join, 관계 대수의 product를 생각하면 된다). 이 메소드의 특징은 두 개 이상의 리스트의 모든 조합을 구할 때 사용된다.