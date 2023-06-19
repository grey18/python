#형식1) 변수 = [ 실행문 for ]
x = [2, 4, 1, 5, 7]
#print(x ** 2) # error

lst = [i ** 2 for i in x] # x변량에 제곱 계산
print(lst) # [4, 16, 1, 25, 49]

#형식2) 변수 = [ 실행문 for if ]
#1~10 -> 2의  배수 추출 -> i * 2 -> list 저장
num = list(range(1,11))

lst2 = [i*2 for i in num if i % 2 == 0] #i가 짝수일 때 곱하기 2
print(lst2) # [4, 8, 12, 16, 20]

'''
tuple 특징
- 순서존재(index 사용 가능)
- 수정 불가
- 문자열 원소 표현
- list 보다 속도 빠름
- 관련 함수 적음
형식) (원소1, 원소2, ...n)
'''

#(1) 원소가 한 개인 경우
t = (10,)
print(t)

#(2) 원소가 여러 개인 경우
t2 = (1, 2, 3, 4, 5, 3)
print(t2)

#(3) 튜플 색인
print(t2[0], t2[1:4], t2[-1])

#(4) 수정 불가!
#t2[0] = 10 # error

# 요소 반복
for i in t2:
    print(i, end=' ')

# 요소 검사
if 6 in t2:
    print("6 있음")
else:
    print("6 없음")

#(1) 튜플 자료형 변환
lst = list(range(1,6))
t3 = tuple(lst)
print(t3)

#(2) 튜플 관련 함수
print(len(t3), type(t3)) # 5<class 'tuple'>
print(t3.count(3)) # 1 / 원소 '3'의 개수를 카운트
print(t3.index(4)) # 3 / 원소 '4'의 위치를 출력