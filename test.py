
# print("hello world!")

#주석은 컴퓨터가 번역하지않는 문장
#즉, 사람만 읽으라고 적어놓은 설명문

# 파이썬은 주석을 #으로 표시한다

# 문자열 선언 (선언 == 만든다)
str = "Hello world"
str2 = 'hello world'
str3 = """hello world"""
str4 = '''hello world'''
str5 = '''It's apple'''
# print(str)

str = "안녕"
str2 = "지원"
str3 = str + str2
# print(str3)

# len이라는 이름을 가진 함수는 길이를 알려주는 친구다.
# print(len(str3))


a = 10
b = "str"
c = 1.3
d = False
e = [1,2,3]
f = {"1":"name"}
g = {1,2,3,4,5}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

# val = int(input("나이를 입력하세요 : "))
# print(val)

# print(type(val))

# str()
# list()
# int()
# float()

a, b, c = map(int,input("값 게개 입력").split(","))
print("a : ", a)
print("b : ", b)
print("c : ", c)