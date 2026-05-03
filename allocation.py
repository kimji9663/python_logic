# 변수 할당 확인용 소스 파일
"""
파이썬에서의 변수 공간에 값 기록하는 메모리 할당(Memory allocation)
- 파이썬의 변수 할당은 동적 할당임
- 동적(Runtime 시 : 실행 시) 메모리(RAM)에 변수 공간 만들고 값을 기록하는 것
- 코드 구문 :
    변수명 = 기록할 값
    변수명 = 계산식
- 주의사항
    변수명(= 값 없으면 에러, 할당 안된 상태임)
"""

num = 1 + 2
print('num 변수가 가진 값 :', num)

# 변수 할당 시 = (대입연산자) 사용함
# 대입연산자는 반드시 왼쪽에 변수, 오른쪽에 값 또는 계산식 위치함(아닐 시 에러)
# 100 = a # SyntaxError

# 한번에 여러개의 변수 값을 할당해야 하는 경우
# x = 10
# y = 20
# z = 30
x, y, z = 10, 20, 30
print(x, y, z)

print(x, y, z, sep='|', end=" 그리고 ") # sep : 구분자(출력값들 사이에 구분할 문자 지정 가능)
print(x, y, z, sep=',', end=None)

# 한 개의 값을 여러 변수에 할당해야 하는 경우
k = m = n = 77 # 77을 n에 할당-> n을 m에 할당-> m을 k에 할당
print(k, m, n, sep=',')

# 한 줄(line)에 하나의 문장 작성이 원칙
# but, 필요 시 한 줄에 여러 문장을 작성한다면, 세미콜론(;)으로 구분
# num1 = 12
# num2 = 24
num1 = 12; num2 = 24
print(num1, num2)

# 두 변수의 값 교환
first, second = 123, 456
print('first :', first, 'second :', second)

first, second = second, first # swap 공식이 필요없음. 간단하게 값 교환 가능.
print('first :', first, 'second :', second)

# = (순수대입연산자)
# 복합대입연산자 : 산술대입연산자가 주로 사용됨
# 파이썬의 산술연산자 : +, -, *, /(나누었을때 몫이 실수형), //(나누었을때 몫이 정수형), %(mod, 나머지), **(제곱연산자)
# +=, -=, *=, /=, //=, **= 
# 메모리의 번수 공간에 직접 연산하므로, 연산처리 속도가 빠름(권장)
value = 100
print('value :', value)

# 10 증가 : value = value + 10 보다 빠름
value += 10
print('value :', value)

# 5 감소 : value = value - 5 보다 빠름
value -= 5
print('value :', value)

# 2배 증가 : value = value * 2 보다 빠름
value *= 2
print('value :', value)

# 2배 감소 : value = value / 2 보다 빠름
# value /= 2 # 나머지가 있든 없든 실수형으로 출력 : 105.0
value //= 2 # 나머지가 있든 없든 정수형으로 출력 : 105
print('value :', value)

# 제곱연산 : **
value **= 2
print('value :', value)

# 파이썬 코드 문장은 한 줄에 작성이 원칙
# 필요 시 문장이 긴 경우 여러줄로 나누기 가능
# 단, 개행 포인트에 백슬러시 표기(\)
print('파이썬은 인터프리터 언어이다. 스크립트 언어이기도 하다. 해석기로 한 줄씩 읽으면서 실행되는 방식의 언어이다.')

print('파이썬은 인터프리터 언어이다. ' \
'스크립트 언어이기도 하다. ' \
'해석기로 한 줄씩 읽으면서 실행되는 방식의 언어이다.')