'''조건식 형식)
if 조건식 :
    실행문1 #파이썬에서는 중괄호로 묶지 않고 들여쓰기 여러 실행문 작성 가능!
else :
    실행문2
'''

#단일 조건문
#1)
var =10 
if var >= 5 : #조건식
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

print('항상 실행')

#2)
#100~85 : '우수', 84~70 : '보통', 69이하 : '저조'
score = int(input('점수 입력 : '))
if score >=85 and score <=100:
    print('우수')
else:
    if score >= 70:
        print('보통')
    else:
        print('저조')

#중첩 조건문

score = int(input('점수 입력 : '))
grade = '' #등급

if score >=85 and score <=100:
    grade = '우수'
elif score >= 70:
    grade = '보통'
else:
    grade = '저조'

print('당신의 점수는 %d이고, 등급은 %s'%(score, grade))

#삼항 조건문
'''변수 = 참 if (조건문) else 거짓'''

#(1) 일반 조건문
num = 9
result =0

if num >= 5:
    result = num * 2
else:
    result = num + 2

print('result =', result)

#(2) 3항 연산자
#형식) 변수 = 참 if (조건문) else 거짓
result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2)