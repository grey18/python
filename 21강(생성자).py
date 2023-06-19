'''
생성자

참조 변수 = 클래스이름(실인수)
'''
#(1) 생성자 이용 멤버변수 초기화
class multiply:
    x = y = 0 #멤버 변수
    def __init__(self, x, y): #객체만 생성
        self.x = x
        self.y = y
    def mul(self):
        return self.x * self.y
    
obj = multiply(10, 20) #생성자
print('곱셈 =', obj.mul())

#(2) 메서드 이용 멤버변수 초기화
class multiply2:
    x = y = 0 #멤버 변수
    def __init__(self):
        pass
    def data(self, x, y):  #메서드 : 멤버 변수 초기화
        self.x = x
        self.y = y
    def mul(self): #메서드 : 곱셈
        return self.x * self.y

obj = multiply2() #기본 생성자
obj.data(10, 20) #동적 멤버 변수 생성
print('곱셈 =', obj.mul())

'''
self
멤버 변수와 메서드 호출
self.멤버 변수
self.메서드()
'''

class multiply3:
    #멤버 변수 없음
    #생성자 없음
    #동적 멤버 변수 생성/초기화
    def data(self, x, y):
        self.x = x
        self.y = y
    def mul(self): #곱셈 연산
        result = self.x * self.y
        self.display(result) #메서드 호출
    def display(self, result):
        print("곱셈 = %d" %(result))

obj = multiply3() #기본 생성자
obj.data(10, 20)
obj.mul()

'''
클래스 멤버
'''

class DatePro:
    #(1) 멤버 변수
    content = "날짜 처리 클래스"
    #(2) 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    #(3) 객체 메서드(instance method)
    def display(self):
        print("%d-%d-%d" %(self.year, self.month, self.day))
    #(4) 클래스 메서드(class method)
    @classmethod # 함수 장식자
    def date_string(cls, dateStr): #19951025
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]
        print(f"{year}년 {month}월 {day}일")

#(5) 객체 멤버
date = DatePro(1995, 10, 25) #생성자
print(date.content) #날짜 처리 클래스
print(date.year) #1995
date.display() #1995-10-25

#(6) 클래스 멤버
print(DatePro.content) #날짜 처리 클래스
print(DatePro.year) #AttributeError
DatePro.date_string('19951025')