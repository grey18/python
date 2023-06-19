#1. 문자열 유형
oneLine = "this is on line string" # this is one line string
multiline = """this is 
multi line
string"""
multiline2 = "this is\nmulti line\nstring"

print(oneLine)
print(multiline)
print(multiline2)

# 2. 색인과 문자열 연산 : +, *

#1) 문자열 색인
string = "PYTHON"
print(string[0]) # P
print(string[5]) # N
print(string[-1]) # N
print(string[-6]) # P

#2) 문자열 연산
print("python" + "program") # 결합연산자
#python-3.7.exe
#print("python-" + 3.7 + ".exe") #error
print("python-" + str(3.7) + ".exe") # python-3.7.exe

print("-"*30) #반복연산자

# 3) 문자열 슬라이싱(slicing)
#lineStr = "this is one line string"

#왼쪽 기준
print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0:4]) # 1~4문자[start:end-1] - this
print(oneLine[:4]) # [:end-1] : 처음부터 ~
print(oneLine[:]) #전체 원소 : this is one line string
print(oneLine[::2]) # 2의 배수 index : ti soeln tig

#오른쪽 기준

print(oneLine[0:-1:2])
print(oneLine[-6:-1]) #strin
print(oneLine[-1:-6:-2])
print(oneLine[-6:]) #[start:end] - string

# 부분 문자열 생성
subString = oneLine[-11:]
print(subString) # line string

# 3. escape 처리 : 특수기능('', "", \n, \t)으로 부터 탈출[차단]

#escape 기능 차단
print('escape 문자 차단')
print('\n출력 이스케이프 문자') # \n : 줄 바꿈 기능

print('\\n출력 이스케이프 차단1') # escape 기능 차단1 - \
print(r'\n출력 이스케이프 차단2') # escape 기능 차단2 - r

#경로 표현 : C:\Python\test
print('path =', 'C:\python\test')
print('path =', 'C:\\Python\\test')
print('path =', r'C:\Python\test')
