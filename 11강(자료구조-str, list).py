'''
string 객체 특징
- 문자들의 모음
- 일정한 순서를 갖는다
- 색인을 이용하여 원소를 참조할 수 있다
'''

help(str) # Help on class str in module builtins:

#str 클래스 형식
str_var = str(object='string')
print(str_var)
print(type(str_var))
print(str_var[0])
print(str_var[-1])

#str 클래스 간편 형식
str_var2 = 'string'
print(str_var2)
print(type(str_var2))
print(str_var2[0])
print(str_var2[-1])

#(1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)
print(type(lst))
for i in lst:
    print(lst[:i]) #i 전까지
'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
'''

# (2) 단일 list 색인
x = list(range(1, 11))
print(x)
print(x[:5])
print('index 2씩 증가')
print(x[::2]) #홀수 색인/0번째 배열값은 1
print(x[1::2]) #1부터 시작하는 짝수 색인/1번재 배열값은 2

#중첩 리스트

# (1) 단일 list 객체 생성
a = ['a', 'b', 'c'] # list 생성
print(a)

# (2) 중첩 list 객체 생성
b = [10, 20, a, 5, True, '문자열'] # 서로 다른 type 가능
print(b[0]) #10
print(b[2]) # ['a', 'b', 'c'] -> 중첩 list
print(b[2][0]) #a -> 중첩 list 0번째 원소
print(b[2][1:]) # ['b', 'c'] -> 중첩 list 2번 이후 원소

# list 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y #new object
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# list 확장
x.extend(y) # x확장
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# list 추가
x.append(y) # x추가
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# list 두 배 확장
lst = [1, 2, 3, 4] # list 생성
result = lst * 2 # 각 원소 연산 안됨
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]

# (1) list 정렬
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]
result.sort() # 오름차순 정렬
print(result) # [1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse = True) # 내림차순 정렬
print(result) # [4, 4, 3, 3, 2, 2, 1, 1]

#(2) list 요소 검사
import random
r = [] # 빈 list
for i in range(5):
    r.append(random.randint(1,5))

print(r)
if 4 in r:
    print('있음')
else:
    print('없음')