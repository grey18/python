#while문
#(1) 카운터와 누적변수
cnt = tot = 0
while cnt < 5 : #true이므로 loop 수행
    cnt += 1 #카운터 변수
    tot += cnt #누적 변수
    print(cnt, tot)

#[실습] 1~200 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = []

while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt #누적 변수
        dataset.append(cnt) #cnt 추가

print('1~100 사이 3의 배수 합 = %d' %tot)
print('dataset =', dataset)

#무한 loop : exit 조건식 포함
numData = []

while 1:
    num = int(input("숫자 입력 : "))
    if num % 10 == 0: #exit 조건식
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)

print(numData)

#(1) random module 추가
import random #random 사용 전 호출 필요!
help (random) #모듈 도움말

#(2) random 모듈의 함수 도움말
help (random.random)

#(3) 0~1 사이 난수 실수
random.seed(123)
r = random.random()
print('r=', r)

#[실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.01:
        break #loop exit
    else:
        cnt += 1

print('난수 개수=', cnt)

#(1) random 관련 함수 도움말
help(random.randint)
help(random.choice) #모집단에서 k 크기 목록 반환

#(2) 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동', '이순신', '유관순']
print(names) #전체 이름
print(names[2]) #특정 이름 출력

#(3) list에서 자료 유무 확인하기
if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

#(4) 난수 정수로 이름 선택하기
idx = random.randint(0, 2)
print(names[idx])

'''
continue, break
    - continue : 계속 반복, 다음 문장 skip
    - break : 탈출(exit)
'''

i = 0
while i < 10:
    i += 1 #카운터
    if i == 3:
        continue # 1 2 4 5 6 7 8 9 10 -> 다음 문장 skip
    if i == 6:
        break # 1 2 4 5 -> exit
    print(i, end='')