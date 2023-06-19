"셋 객체 특징"
'''변수 = {값1, 값2, 값3, ... 값n}'''
#(1) 중복 불가
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)

# 요소 반복
for d in s:
    print(d, end=' ') # 1 3 5

print()

#(3) 집합관련 함수
s2 = {3, 6}
print(s.union(s2)) # 합집합
print(s.difference(s2)) # 차집합
print(s.intersection(s2)) # 교집합

#(4) 추가, 삭제 함수
s3 = {1, 3, 5}
print(s3)

s3.add(7) # 원소 추가
print(s3)

s3.discard(3) # 원소 삭제
print(s3)

"중복 원소를 갖는 리스트"
gender = ['남', '여', '남', '여']

#중복 원소 제거
sgender = set(gender) #list -> set
lgender = list(sgender) # set -> list
print(lgender)

print(lgender[1])

"딕트 객체 특징"
'''변수 = {'키' : '값', '키' : '값', ... '키' : '값'}'''

#(1) dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

#(2) dict 생성 방법2
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

#(3) 원소 수정, 삭제, 추가

#원소 수정
person['age'] = 45
print(person)

#원소 삭제
del person['address']
print(person) # {'name':'홍길동', 'age':45}

#dict 원소 추가
person['pay'] = 350
print(person) # {'name':'홍길동', 'age':45, 'pay':350}

#(1) 요소 검사
print(person['age'])
print('age' in person)

#(2) 요소 반복
for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)

"단어 출현빈도수 구하기"

#(1) 단어 데이터 셋
charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}

#(2) get() 함수 이용 : key 이용 value 가져오기
for key in charset:
    wc[key] = wc.get(key, 0) + 1

print(wc)