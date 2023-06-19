'''
캡슐화
'''

class Account:
    #(1) 은닉 멤버 변수
    __balance = 0 #잔액
    __accName = None #예금주
    __accNo = None #계좌 번호
    #(2) 생성자 : 멤버 변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal #잔액 초기화
        self.__accName = name #예금주
        self.__accNo = no #계좌 번호
    #(3) 계좌 정보 확인: Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo
    #(4) 입금하기 : Setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return #종료(exit)
        self.__balance += money
    #(5) 출금하기 : Setter
    def withdraw(self, money):
        if self.balance < money:
            print('잔액 부족')
            return #종료(exit)
        self.__balance -= money
#(6) object 생성
acc = Account(1000, '홍길동', '125-152-4125-41') # 생성자
#(7) Getter 호출
acc.__balance # 오류(Error)
bal = acc.getBalance()
print('계좌 정보: ', bal)
#(8) Setter 호출
acc.deposit(10000) #10,000원 입금
bal = acc.getBalance()
print('계좌 정보: ', bal) #입금 확인

'''
클래스의 상속
'''

#(1) 부모 클래스
class Super:
    #생성자 : 동적멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #메서드
    def display(self):
        print('name : %s, age : %d'%(self.name, self.age))

sup = Super('부모', 55)
sup.display() #부모 멤버 호출

#(2) 자식 클래스
class Sub(Super): #클래스 상속
    gender = None #자식 멤버
    #(3) 생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #(4) 메서드확장
    def display(self):
        print('name : %s, age : %d, gender : %s'%(self.name, self.age, self.gender))

sub = Sub('자식', 25, '여자')
sub.display() #자식 멤버 호출

'''
super 클래스
형식) 
super().__init__() #부모 클래스 생성자 호출
'''

#(1) 부모 클래스
class Parent:
    #생성자 : 객체 + 초기화
    def __init__(self, name, job):
        self.name = name
        self.job = job
    #멤버 함수(method)
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

p = Parent('홍길동', '회사원')
p.display()

#(2) 자식 클래스
class Children(Parent): #Parent 클래스 상속
    gender = None #자식 클래스 멤버변수 추가
    #(3) 자식 클래스 생성자
    def __init__(self, name, job, gender):
        self.gender = gender
        #부모 클래스 생성자 호출
        super().__init__(name, job) #name, job
    def display(self):
        print('name : {}, job : {}, gender : {}'.format(self.name, self.job, self.gender))

c = Children('홍길동', '회사원', '남자')
c.display()

'''
메서드 재정의
'''

#(1)부모 클래스
class Employee:
    name = None
    pay = 0
    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass
#(2) 자식 클래스 : 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name) #부모 생성자 호출
    def pay_calc(self, base, bonus):
        self.pay = base + bonus #급여 = 기본급 + 상여금
        print('총 수령액 : ', format(self.pay))
#(3) 자식 클래스 : 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name) #부모 생성자 호출
    def pay_calc(self, tpay, time):
        self.pay = tpay + time # 급여 = 작업시간 * 시급
        print('총 수령액 :', format(self.pay))
#(4) 객체 생성
p = Permanent("이순신")
p.pay_calc(3000000, 200000)
t = Temporary("홍길동")
t.pay_calc(15000, 80)