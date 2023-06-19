'''
문자열 찾기
'''

import re #모듈 추가 - 방법1
from re import findall #모듈 추가 - 방법2

st1 = '1234 abc홍길동ABC_555_6 이사도시'

#(1) 숫자 찾기
print(findall('1234', st1))
print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
print(findall('\\d{3,}', st1))

#(2) 문자열 찾기
print(findall('[가-힣]{3,}', st1))
print(findall('[a-z]{3}', st1))
print(findall('[a-z|A-Z]{3}', st1))

#(3) 특정 위치의 문자열 찾기
st2 = 'test1abcABC123mbc45test'

#접두어/접미어
print(findall('^test', st2)) #접두어
print(findall('st$', st2)) #접미어

#종료 문자 찾기 : abc, mbc
print(findall('.bc', st2))

#시작 문자 찾기
print(findall('t.', st2))

#(4) 단어 찾기(\\w) - 한글+영문+숫자
st3 = 'test^홍길동abc대한*민국123$tbc'
words = findall('\\w{3,}', st3)
print(words)

#(5) 문자열 제외 : x+(x가 1개 이상 반복)
print(findall('[^^*$]+', st3)) #특수문자 제외

'''
문자열 검사
'''

from re import match

#(1) 패턴과 일치된 경우
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)
if result: #object
    print('주민번호 일치')
else: #null
    print('잘못된 주민번호')

#(2) 패턴과 불일치된 경우
jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result) #None

if result: #object
    print('주민번호 일치')
else: #null
    print('잘못된 주민번호')

'''
문자열 치환
'''

from re import sub

st3 = 'test^홍길동abc대한*민국123$tbc'

#(1) 특수문자 제거
text1 = sub('[\^*$]+', '', st3)
print(text1)

#(2) 숫자 제거
text2 = sub('[0-9]', '', text1)
print(text2)