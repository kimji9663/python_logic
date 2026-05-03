# 파이썬이 제공하는 내장함수 확인용 소스파일

'''
파이썬이 제공하는 내장함수는 기본으로 제공됨
별도의 import가 필요없음
max, min, type, len, range, str, int, float, print, input 등
'''

# type(값|변수명) => 값의 자료형을 리턴하는 함수(class<자료형>)
# len(값|변수명) => 길이(저장된 값의 갯수)
a = 'abcd'
b = [1, 2, 3, 4, 5] # 군집자료형(list)
print(type(a), len(a), type(b), len(b)) # <class 'str'> 4 <class 'list'> 5

# max(값들|변수) => 가장 큰 값(최대값) 리턴 함수
print(max('abcdefg')) # 가장 큰 값 : g
print(max('123456789')) # 가장 큰 값 : 9

print(min('abcdefg')) # 가장 큰 값 : a
print(min('123456789')) # 가장 큰 값 : 1

# 주석(comment): 코드의 내용 이해를 돕기 위한 설명 문구
# 한 줄 주석
'''
여러 줄 주석
파이썬에서는 single quotation 이든 double quotation 이든 
동일하게 취급
'''

# abs함수(값|변수) : 절대값 리턴
print(abs(-10)) # 10 출력(음수의 절대값 => 양수)

# 파이썬에서는 변수는 반드시 값을 가져야 생성됨 (생성 == 메모리에 할당)
# num
# print(num)

# 파이썬에서는 변수에 기록할 값의 종류(data type : 자료형)를 정하지 않는다.
# Java : 자료형 변수명 = 기록할 값; # 일반적인 언어의 변수 만드는 방법
# Python : 변수명 = 기록할 값 # 파이썬은 동적할당. 기록된 값에 따라 자료형이 정해짐
value = 100
print(value, type(value))

value = 'python'
print(value, type(value))

value = False
print(value, type(value))

# 변수 제거 : del 변수명
# del value
# print(value, type(value))