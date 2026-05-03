# 식별자 : 개발자가 지어주는 이름
# 변수(varialble) : 프로그램 구동 시 메모리(RAM)에 값 기록하는 공간(방)
# 함수(function) : 반복되는 코드를 분리 작성하여 이름을 붙인 것(소스 코드의 조각 코드)
# 모듈(module) : 함수들을 모아놓은 파일
# 클래스(class) : 파이썬은 객체지향형 스크립트 언어. 첫글자는 대문자로 표기

# 이름 작성 규칙 : 식별자 조건(Naming Rule)
# 1. 대소문자 구분 : name, Name, NAME 같이 사용가능
NAME = '홍길동'
name = '이순신'
Name = '황진이'
print(NAME, name, Name, type(NAME))

# 2. 이름 첫글자에 숫자 사용 X
# 1num = 100
# print(1num, type(1num))

# 3. 이름 첫글자는 문자 또는 _만 허용
_score = 100.0
print(_score, type(_score))

# 4. _를 제외한 기호문자, 공백 사용 X
# num& = 12
# print(num&)

# 5. 비교관계연산자는 결과값이 논리값이다.
num1 = 10
num2 = 20
print(num1 < num2) #True

# 6. 예약어(프로그램 언어가 사용하기 위해 별도로 정해 놓은 단어들)는 이름으로 사용할 수 없다.
# 예약어 확인 : keyword 모듈에서 제공 => import 해서 사용함
import keyword
print(len(keyword.kwlist))
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
