def fun1():
    a = input("당신은 누구입니까? ")
    print("안녕 %s" % a)

def fun2():
    print("안녕하세요.\n파이썬을 사용 중 입니다.")

def fun3():
    str = "Hello"
    flag = True
    age = 20
    score = [70, 80, 90]
    student = {"name":"JW", "age":24}
    val = (10,)
    val2 = {1, 2, 3, 2, 1}

    print(type(str))
    print(type(flag))
    print(type(age))
    print(type(score))
    print(type(student))
    print(type(val))
    print(type(val2))

def fun4():
    str = "Hello"
    score = [70, 80, 90]
    student = {"name":"JW", "age":24}
    val = (10,)
    val2 = {1, 2, 3, 2, 1}

    print(len(str))
    print(len(score))
    print(len(student))
    print(len(val))
    print(len(val2))

def fun5():
    str = "hello world"
    print(str[:5])
    print(str[-5:])

def fun6():
    age = 2024 - int(input("출생년도를 입력하세요 : "))
    print("당신은 %d살 입니다" % age)

def fun7():
    num = int(input("숫자를 입력하세요 : "))

    if(num % 2 == 0):
        print("짝수입니다.")
    else:
        print("홀수입니다.")

def fun8():
    kor = int(input("국어 점수를 입력해주세요 : "))
    math = int(input("수학 점수를 입력해주세요 : "))
    eng = int(input("영어 점수를 입력해주세요 : "))
    average = (kor + math + eng)/3

    print("평균 점수는", average, "점 입니다.")

def fun9():
    str1 = input("첫 번째 문자열을 입력하세요 : ")
    str2 = input("두 번째 문자열을 입력하세요 : ")

    print("결과 : ", str1 + str2)

def fun10():
    str = input("문자열을 입력하세요 : ")
    num = int(input("반복횟수를 입력하세요 : "))

    print(str * num)

def fun11():
    ramyeon, snack, drink = input("라면, 과자, 음료의 구매 개수를 입력해주세요 : ").split(",")
    total = int(ramyeon)*1000 + int(snack)*800 + int(drink)*1500

    print("총 금액은 %s 원 입니다" % total)

def fun12():
    print(5 % 3)

def fun13():
    num1 = 0
    num1 += 3 #== (num1 = num1 + 3)

def fun14():
    a = int(input("첫번째 수 : "))
    b = int(input("두번째 수 : "))

    print("더하기 : ", a+b)
    print("빼기 : ", a-b)
    print("곱하기 : ", a*b)
    print("나누기 : ", a/b)
    print("몫 : ", a//b)
    print("나머지 : ", a%b)
    print("제곱 : ", a**b)

def fun15():
    # Q1
    mylist = [65, 80, 55]
    print("Q1 : ", mylist)

    # Q2
    print("Q2 : ", mylist[1])

    # Q3
    mylist.append(100)

    # Q4
    mylist[3] = 90

    # Q5
    mylist.sort()
    print("Q5 : ", mylist)

    mylist.sort(reverse=True)
    print("Q5 : ", mylist)

    # Q5 - 1
    mylist.insert(2, 30)
    print("Q5-1 : ", mylist)

    # Q6
    print(mylist[-1])
    mylist.pop()
    
    print("Q6 : ", mylist)

    # Q7
    print("Q7 : ", mylist.index(30))

    # Q8
    newlist = [30, 30, 100]
    mylist += newlist
    print("Q8 : ", mylist)

    # Q9
    cnt = 0
    for i in range(0,len(mylist)):
        if(mylist[i]==30):
            cnt += 1
    print("Q9 : ", cnt)
    
    # Q10
    mylist.remove(30)
    print("Q10 : ", mylist)

    # Q11
    index_65 = mylist.index(65)
    del mylist[index_65]
    print("Q11 : ", mylist)

def fun16():
    mytuple = (1, 2, 3)
    print(mytuple)

    # Q1
    print(f"({mytuple[0]}, {mytuple[1]})")

    # Q2
    solotuple = (30,)
    print(solotuple)

    # Q3
    tuple1 = (1, 2)
    tuple2 = ('a', 'b')

    tuple1 += tuple2
    print(tuple1)

    # Q4
    tuple12 = (1, 2)
    print(tuple12 * 5)

    # Q5
    print("튜플보다 리스트를 훨씬 많이 써서 or 리스트와 사용법이 비슷해서 or 출제자가 귀찮아서")

def fun17():
    newdict = {'name': '정지원', 'age': 20, 'stdNum': 202345047}
    newdict['grade'] = 3
    print(newdict['name'])
    print(newdict.keys())
    print(newdict.values())
    print(newdict.items()) # key, value 쌍 튜플로 묶어서 제공
    print(newdict)

    print('name' in newdict)
    print('class' in newdict)

    del newdict['grade']
    print(newdict)

    newdict.clear()
    print(newdict)


# --------------------------------------------------------------------

def fun_9():
    a, b = input("두 수를 공백으로 구분하여 입력하세요 : ").split(" ")
    a = int(a)
    b = int(b)

    if(a>=b): print(a)
    else: print(b)

def fun_8():
    num = int(input("20보다 작은 숫자를 입력하세요 : "))
    if(num>=20):
        print("Too High")
    else:
        print("Thank you")

def fun_7():
    color = input("좋아하는 색을 영어로 입력하세요 : ")
    if((color == "red") or (color == "Red") or (color == "RED")):
        print("I like red too")
    else:
        print("I don't like that color, I prefer red")

def fun_6():
    mylist = [1,2,3,4,5]
    print(mylist)

def fun_5():
    total = 0
    for i in range(1,11):
        total += i
    print(total)

def fun_4():
    total = 0
    num = int(input("숫자를 입력하세요 : "))
    for i in range(1,num+1):
        total += i

    print(total)

def fun_3():
    mylist = []
    mylist = input("여러 숫자를 띄어쓰기로 구분하여 입력하세요 : ").split(" ")

    for i in range(0, len(mylist)):
        mylist[i] = int(mylist[i])

    mylist.sort()

    print("최대값 : ", mylist[-1])
    print("최소값 : ", mylist[0])

def fun_2():
    for i in range(1,6):
        print("*" * i)

def fun_1():
    def repeat():
        str = input("입력: ")
        if(str == "python"):
         print("good")

        else:
            repeat()

    repeat()


fun17()
