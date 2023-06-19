'''
함수 형식)
def 외부 함수(인수):
    변수 선언
    def 내부 함수(인수):
        실행문
        return 값
    return 내부함수
'''

'''
클래스 형식)
class 클래스명:
    변수 선언
    def 생성자(인수):
        실행문
    def 함수명(인수):
        실행문
'''

#(1) 함수 정의
def calc_func(a, b): #외부 함수
    x=a #변수 선언:자료 저장 #10
    y=b #20
    def plus(): #내부 함수
        p =x + y
        return p
    def minus(): #내부 함수
        m = x - y
        return m
    return plus, minus

#(2) 함수 호출
p, m = calc_func(10, 20)
print('plus =', p())
print('minus =', m())

#(3) 클래스 정의
class calc_class:
    x = y = 0 #클래스 변수:자료 저장
    def __init__(self, a, b): #생성자:객체 생성 + 멤버변수 초기화
        self.x = a #10
        self.y = b #20
    def plus(self): #클래스 함수
        p = self.x + self.y #변수 연산
        return p
    def minus(self): #클래스 함수
        m = self.x - self.y #변수 연산
        return m

#(4) 객체 생성
obj = calc_class(10, 20)

#(5) 멤버 호출
print('plus =', obj.plus()) #plus = 30
print('minus =', obj.minus()) #minus = -10

'''
클래스 구성요소
'''

class Car:
    cc = 0 #(1) 멤버변수 #엔진 cc
    door = 0 #문짝 개수
    carType = None #null
    def __init__(self, cc, door, carType): #(2) 생성자
        self.cc = cc #멤버 변수 초기화
        self.door = door
        self.carType = carType #승용차, suv
    def display(self): #(3) 메서드
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s" %(self.cc, self.door, self.carType))

car1 = Car(2000, 4, "승용차") # 객체 생성 + 초기화
car2 = Car(3000, 5, "SUV")

#(5) 멤버 호출: object.member()
car1.display() #car1 멤버 호출
car2.display() #car2 멤버 호출