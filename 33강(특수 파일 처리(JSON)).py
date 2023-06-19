'''
JSON 파일
인코딩
형식) json.dumps(객체)
디코딩
형식) json.loads(json문자열)
'''

#(1-1) json 인코딩
user = {'id' : 1234, 'name' : '홍길동'} #python dict
print(type(user)) # <class 'dict'>
print(user['name']) #홍길동
#(1-2) json 인코딩
jsonString = json.dumps(user, ensure_ascii = False) # ASCII 인코딩 방식 적용 안 함
#문자열 출력
print(jsonString) # {'id' : 1234, 'name' : '홍길동'}
print(type(jsonString)) # class str
print(jsonString['name']) #Error 발생
#(2) json 디코딩
pyObj = json.loads(jsonString)
print(type(pyObj)) #<class 'dict'>
#Dict 자료 확인
print(pyObj ['name']) #홍길동
for key in pyObj:
    print(key, ':', pyObj[key])