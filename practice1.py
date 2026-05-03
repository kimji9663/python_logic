# 문제1
x = 'abc123'
print(len(x), type(x))
print(max(x), min(x))
# print(int(x)) # 문자로 변환불가

# 문제2
y = 'AB'
# print(range(y[0]))
y = ord(y[0]), ord(y[1])
print(y, sep=" ")
print(type(y))