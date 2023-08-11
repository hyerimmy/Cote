# 절대값 abs()

## abs(x)

절대값을 구할때 abs라는 이름의 함수를 사용합니다.

절대값을 구하고 싶은 수를 매개변수로 집어 넣고,

반환형으로 넣은 수의 절대값이 나옵니다.



매개변수로 넣은 숫자가 변하는 것이 아니라. 넣은 숫자는 가만히 있고

넣은 숫자의 절대값이 반환되는 것입니다.

## 예제
```python
# 1. 정수
num1 = -99
num2 = 99
print(f'abs({num1}) = {abs(num1)}') # abs(num1)
print(f'abs({num2}) = {abs(num2)}') # abs(num2)
 
# 2. 실수
num3 = -99.99
num4 = 99.99
print(f'abs({num3}) = {abs(num3)}') # abs(num3)
print(f'abs({num4}) = {abs(num4)}') # abs(num4)
 
# 3. 0의 절대값은? 0이겠죠
num5 = 0
num6 = 0.0
print(f'abs({num5}) = {abs(num5)}') # abs(num5)
print(f'abs({num6}) = {abs(num6)}') # abs(num6)
```