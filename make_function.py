# 파이썬에서 함수 만들기 연습용 소스파일
# def 키워드 사용,  맨 뒤에 반드시 :을 붙임
# 함수명 아랫줄은 **반드시 들어쓰기**
'''
def 함수명(매개변수, ...):
    함수코드 작성
    return 결과값
'''

def hello(name):
    print(f'✨안녕하세요! {name}님😊')
    return

def chek_type():
    a = 1
    b = '1'
    c = 1.1
    d = True
    # 파이썬은 정수, 실수의 바이트 크기제한이 없다.
    e = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    f = 4 + 1j
    print(type(a), type(b), type(c), type(d), type(e), type(f))
    return


# 파이썬에서의 main은 아래와 같이 표현함
if __name__ == '__main__':
    # 프로그램 시작하면 실행할 내용이나 함수를 구문으로 작성함
    print('✨프로그램 시작!')
    
    # 함수 실행
    # hello('홍길동')
    # chek_type()

    a = '안녕'
    b = '하세요😊'
    print(a + b) # '문자1' + '문자2' = '문자1문자2' : 문자 합치기(string concaternation)
    
    print('프로그램 종료!✨')
