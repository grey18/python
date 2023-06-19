'''
다형성
'''

#(1) 부모 클래스
class Flight:
    #부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')
#(2) 자식 클래스 : 비행기
class Airplane(Flight):
    #함수 재정의
    def fly(self):
        print('비행기가 날다.')
#(2) 자식 클래스 : 새
class Bird(Flight):
    #함수 재정의
    def fly(self):
        print('새가 날다.')
#(2) 자식 클래스 : 종이비행기
class PaperAirplane(Flight):
    #함수 재정의
    def fly(self):
        print('종이 비행기가 날다.')
#(3) 객체 생성
#부모 객체 = 자식 객체(자식1, 자식2)
flight = Flight() #부모 클래스 객체
air = Airplane() #자식1 클래스객체
bird = Bird() #자식2 클래스 객체
paper = PaperAirplane() #자식3 클래스 객체

#(4) 다형성
flight.fly() #날다, fly 원형 메서드

flight = air
flight.fly() #비행기가 날다

flight = bird
flight.fly() #새가 날다

flight = paper
flight.fly() #종이 비행기가 날다

'''
내장 클래스

호출 형식 1) import 모듈명 2) from 모듈명 import 클래스명1, 클래스명 2, ...

builtins 모듈 내장 클래스
'''

#(1) 리스트 열거형 객체 이용
lst = [1, 3, 5]
for i, c in enumerate(lst):
    print('색인 :', i, end=', ')
    print('내용 :', c)
#(2) 튜플 열거형 객체 이용
dit = {'name' : '홍길동', 'job' : '회사원', 'addr' : '서울시'}
for i, k in enumerate(dit):
    print('순서 :', i, end=', ')
    print('키 :', k, end=', ')
    print('값 :', dit[k])

#(1) 모듈 내장클래스 import
import datetime #모듈 import
from datetime import date, time
#(2) date 클래스
help(date) #date 클래스 도움말

today = date(2019, 10, 23) # date 객체 생성
print(today) # date 객체 정보
#date 객체 멤버변수 호출
print(today.year) #2019
print(today.month) #10
print(today.day) #23
#date 객체 메서드 호출
w = today.weekday() #Monday == 0 ... Sunday == 6
print('요일 정보 :', w) # 요일 정보
#(3) time 클래스
help(time) #time 클래스 도움말

currTime = time(21, 4, 30) #time 객체 생성
print(currTime) #time 객체 정보
#time 객체 멤버변수 호출
print(currTime.hour) #21
print(currTime.minute) #4
print(currTime.second) #30
#time 객체 메서드 호출
isoTime = currTime.isoformat() #HH:MM:SS
print(isoTime)