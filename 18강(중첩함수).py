'''
중첩함수
def 외부함수(인수):
    실행문
    def 내부함수(인수):
        실행문
        return 값
    return 내부함수
'''

#(1) 일급 함수
def a(): #outer
    print('a 함수')
    def b(): #inner
        print('b 함수')
    return b
b=a() #외부 함수 호출 : a 함수
b() #내부 함수 호출 : b 함수

#(2) 함수 클로저
data = list(range(1, 101))
def outer_func(data):
    dataset = data #값(1~100) 생성
    def tot(): #inner
        tot_val = sum(dataset)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataset)
        return avg_val
    return tot, avg #inner 반환

#외부 함수 호출 : data 생성
tot, avg = outer_func(data)

#내부 함수 호출
tot_val = tot()
print('tot=', tot_val)
avg_val = avg(tot_val)
print('avg=', avg_val)

'''
중첩함수 역할
'''

from statistics import mean #평균
from math import sqrt #제곱근

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

#(1) 외부 함수 : 산포도 함수
def scattering_func(data): #outer
    dataSet = data #data 생성
    def avg_func(): #(2) 내부 함수 : 산술평균 반환
        avg_val = mean(dataSet)
        return avg_val
    def var_func(avg): #(3) 내부 함수 : 분산 반환
        diff = [(data - avg) ** 2 for data in dataSet]
        print(sum(diff)) #차의 합
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val
    def std_func(var): #(4) 내부 함수 : 표준편차 반환
        std_val = sqrt(var)
        return std_val
    return avg_func, var_func, std_func #함수 클로저 반환

avg, var, std = scattering_func(data)

#(5) 내부 함수 호출
print('평균: ', avg())
print('분산: ', var(avg()))
print('표준편차: ', std(var(avg())))

'''
획득자, 지정자, nonlocal

nonlocal 형식
def 외부 함수():
    변수명 = 값
    def 내부 함수():
        nonlocal 변수명
'''

#(1) 중첩함수 정의
def main_func(num):
    num_val = num #자료 생성
    def getter(): #획득자 함수, return 있음
        return num_val
    def setter(value): #지정자 함수 인수 있음
        nonlocal num_val #nonlocal 명령어
        num_val = value
    return getter, setter #함수 클로저 반환

#(2) 외부 함수 호출
getter, setter = main_func(100) #num 생성

#(3) 획득자 호출
print('num =', getter()) #획득한 num 확인

#(4) 지정자 획득
setter(200) # num 값 수정
print('num =', getter()) #num 수정 확인

'''
함수 장식자

@함수 장식자
def 함수명():
    실행문
'''

#(1) 래퍼 함수
def wrap(func):
    def decorated():
        print('방가워요!') # 시작 부분엥 삽입
        func() #인수로 넘어온 함수(hello)
        print('잘가요!') #종료 부분에 삽입
    return decorated #클로저 함수 반환

#(2) 함수 장식자 적용
@wrap
def hello():
    print('hi ~ ', "홍길동")

#(3) 함수 호출
hello()