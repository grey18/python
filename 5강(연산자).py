#변수 선언
num1=100
num2=20

#관계연산자
bool_result = num1 == num2
print(bool_result) #False
bool_result = num1 != num2
print(bool_result) #True
bool_result = num1 >= num2
print(bool_result) #True
bool_result = num1 <= num2
print(bool_result) #False

#논리연산자
log_result = num1 >= 50 and num2 <= 10
print(log_result) #False
log_result = num1 >= 50 or num2 <= 10
print(log_result) #True
log_result = num1 >= 50
print(log_result) #True
log_result = not(num1 >= 50)
print(log_result) #False

#대입연산자
i = tot = 10
i += 1 #i = i + 1
tot += i #tot = tot + 1
print(i, tot) #11 21 출력

#같은 줄에 중복 출력
print('출력1', end=',' 'out2') # end='구분자' #출력1,out2 출력 후 같은 줄에 명령어 입력

#2)변수 교체
v1 , v2 = 100, 200
print(v1, v2) #100 200 출력

v2, v1 = v1, v2 #변수 swap
print(v1, v2) #200 100 출력

#3)패킹(packing) 할당
# *기호는 변수에 여러 값을 묶음 할당함
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1, v2) #1 [2, 3, 4, 5]

*v1, v2 = lst
print(v1, v2) #[1, 2, 3, 4] 5

*v1, v2, v3 = lst
print(v1, v2, v3) #[1, 2, 3] 4 5