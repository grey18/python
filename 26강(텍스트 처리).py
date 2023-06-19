'''
텍스트 처리
'''

#re 모듈 관련 함수 import
from re import split, match, compile

#텍스트 자료
multi_line = """http://www.naver.com
http://www.daum.net
www.hongkildong.com"""

#(1) 구분자를 이용하여 문자열 분리
web_site = split("\n", multi_line) #split('pattern', string)
print(web_site)

#(2) 패턴 객체 만들기
pat = compile("http://")

#(3) 패턴 객체를 이용하여 정상 웹 주소 선택하기
sel_site = [site for site in web_site if match(pat, site)]
print(sel_site)

'''
자연어 전처리
'''

#re 모듈관련 함수 import
from re import findall, sub

#텍스트
texts = ['우리나라    대한민국, 우리나라%$만세', 
         '비아그&라 500GRAM 정력 최고!', 
         '나는 대한민국 사람', 
         '보험료 15000원에 평생 보장 마감 임박', 
         '나는 홍길동']
#단계1: 소문자 변경
texts_re1 = [t.lower() for t in texts]
print('texts_rel :', texts_re1)

#단계2: 숫자 제거
texts_re2 = [sub("[0-9]", '', text) for text in texts_re1]
print('texts_re2 :', texts_re2)

#단계3: 문장부호 제거
texts_re3 = [sub('[,.?!:;]', '', text) for text in texts_re2]
print('texts_re3 :', texts_re3)

#단계4: 특수문자 제거: re.sub() 이용
spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
print('texts_re4 :', texts_re4)

#단계5: 영문자 제거
texts_re5 = [''.join(findall("[^a-z]", text)) for text in texts_re4]
print('texts_re5 :', texts_re5)

#단계6: 공백제거
texts_re6 = [' '.join(text.split()) for text in texts_re5] #공백기준 split -> join 결합
print('texts_re6 :', texts_re6)

'''
전처리 함수
'''

#re 모듈관련 함수 import
from re import findall, sub

#텍스트 전처리
texts = ['우리나라    대한민국, 우리나라%$만세', 
         '비아그&라 500GRAM 정력 최고!', 
         '나는 대한민국 사람', 
         '보험료 15000원에 평생 보장 마감 임박', 
         '나는 홍길동']
#(1) 텍스트 전처리 함수
def clean_text(text): #문장 인수
    #1~6단계
    texts_re = text.lower() #소문자 변경
    texts_re2 = sub("[0-9]", '', texts_re)  #숫자 제거
    texts_re3 = sub('[,.?!:;]', '', texts_re2) #문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) #특수문자 제거
    texts_re5 = ''.join(findall("[^a-z]", texts_re4)) #영문자 제거
    texts_re6 = ' '.join(texts_re5.split()) #white space 제거
    return texts_re6 #반환값

#(2) 함수 호출
texts_result = [clean_text(text) for text in texts]
print(texts_result)

#출력 결과
'''
['우리나라 대한민국 우리나라만세', 
'비아그라 정력 최고', 
'나는 대한 민국 사람', 
'보험료 원에 평생 보장 마감 임박', 
'나는 홍길동']
'''