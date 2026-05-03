# 파이썬에서 문자열 다루기

# 파이썬에서 문자열(str)은 시퀀스(sequence: 순차나열)로 취급
# 순차자료형은 나열된 값의 순번(index)이 매겨짐, 0부터 시작
# 동일한 시퀀스 자료형인 리스트(list), 튜플(tuple), 배열(array), 시리즈(series) 들도 동일하게 적용됨

# 문자 선택 연산자(인덱싱) : 문자열변수[인덱스순번]
ss = 'Hi,-python'

print('첫번째 글자: ', ss[0])
print('다섯번째 글자: ', ss[4])
print('뒤에서 첫번째 글자: ', ss[-1])
print('뒤에서 열번째 글자: ', ss[-10])

# 문자열 범위 선택 연산자 (슬라이싱) : 문자열값 부분 추출
# 문자열 변수 [시작인덱스:끝인덱스:간격]
# 끝인덱스는 끝인덱스 -1 위치까지 추출됨
# 간격 생략 시 기본값은 1
# 시작인덱스 생략 시 기본값은 0
# 끝인덱스 생략 시 기본값은 마지막인덱스 + 1 
# 모두 생략했을 때 => ss[:] 문자열 전체
print(ss[0:3]) # 0, 1, 2 => Hi,
print(ss[0:5:2]) # 0, 2, 4 => H,p
print(ss[-6:-1:2]) # pto

# 슬라이싱을 이용하여 문자열을 역순으로 정렬할 수 있음
print(ss)
print(ss[::-1]) # 시작인덱스 생략, 끝인덱스 생략

# 슬라이싱과 연결 연산(+)을 혼합하여 사용 가능
n1 = 'abcdef'
n2 = '12345'
n3 = n1[0:3] + n2[1:] # 끝인덱스 생략, 간격 생략
print(n3)

# 문자열 반복 연산자 : *반복할 횟수
print('✨'*3)

# 문자 처리 내장함수
# upper() : 대문자 변환(영문자일 때에만)
# lower() : 소문자 변환(영문자일 때에만)
tt = 'apple'
print(tt)
print(id(tt)) # tt가 참조하는 문자열의 메모리 위치(주소, 번지로 이해하면 됨)

# 파이썬에서도 기록된 문자열값은 변경할 수 없음(immutable)
# 문자열 기록방식 때문
# 숫자는 숫자 그대로를 기록하기 때문에 변경이 가능함
# 문자열은 자유 메모리 공간에 따로 기록 후 그 공간의 위치 정보를 참조함
# 위치를 참조하기 때문에 수정이 불가
# tt[1] = 'b' # TypeError

tt = 'banana' # 문자가 바뀌는 것이 아닌 기록된 위치 정보가 변경됨(apple => banana)
print(tt)
print(id(tt))

print(tt.upper()) # tt가 참조하는 문자열을 CPU가 읽고 연산장치로 대문자로 변환 후 메모리에 새로 기록함
print(id(tt.upper())) # 주소가 변경되었음이 확인됨 2492571616336 => 2492571616960

tt2 = 'ORANGE'
print(tt2.lower())

# swapcase() 대문자 <-> 소문자
# capitalize() 첫글자 대문자
tt3 = 'tEst STr pYtHoN'
print(tt3) 
print(tt3.swapcase())
print(tt3.capitalize())

# strip(), lstrip(), rstrip()
tt4 = '    test str values   '

print('|', tt4, '|', sep='') # sep='' 출력값들 사이의 공백 구분자 없앰
print('|', tt4.strip(), '|', sep='') # 문자열 앞 뒤(양쪽) 공백 제거
print('|', tt4.lstrip(), '|', sep='') # 문자열 왼쪽 공백 제거
print('|', tt4.rstrip(), '|', sep='') # 문자열 오른쪽 공백 제거

# split() splitlines()
tt5 = 'abc-def-ghi-j'
print(tt5)
print(tt5.split('-')) # - 문자를 기준으로 문자 분리
# 여러 개의 분리된 문자값들을 리스트(list, []로 표현)로 반환

# splitlines() : 줄 단위로 분리해서 리스트로 반환
tt6 = '''
    python
    java
    c++
    javascript
'''

print(tt6)
print(tt6.splitlines())
stt6 = tt6.split()
print(stt6)

# index(), find() : 글자 위치(인덱스, 순번) 조회
# print(tt5.index('k')) # 없는 문자 조회 시 ValueError: substring not found
print(tt5.find('k')) # 없는 문자 조회 시 -1 출력됨(없다는 뜻)

# 이 외의 문자 관련 함수들을 확인하고자 할 경우
print(len(dir(str))) # 81
print(dir(str)) # 81