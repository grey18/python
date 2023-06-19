'''
텍스트 파일 입출력
'''

#(1) 현재 작업디렉터리
import os
print('\n현재 경로 :', os.getcwd())

#(2) 예외처리
try:
    #(3)파일 읽기
    test = open('pywork/test.txt', mode = 'r')
    print(test.read()) #파일 전체 읽기
    #(4)파일 쓰기
    test2 = open('pywork/test2.txt', mode = 'w')
    test2.write('my first text') #파일 쓰기
    #(5) 파일 쓰기 + 내용 추가
    test3 = open('pywork/test3.txt', mode = 'a')
    test3.write('\nmy second text') #파일 쓰기(추가)
except Exception as e:
    print('Error 발생 :', e)
finally:
    test.close() #파일 객체 닫기
    test2.close()
    test3.close()

#파일 읽기 관련 함수
try:
    #(1) read():전체 텍스트 자료 읽기
    test = open('pywork/test.txt', mode = 'r')
    full_text = test.read()
    print(full_text)
    print(type(full_text))
    #(2) readlines():전체 텍스트 줄 단위 읽기
    test = open('pywork/test.txt', mode = 'r')
    lines = [test.readlines()] #list반환
    print(lines)
    print(type(lines)) #<class 'list'>
    print('문단 수 :', len(lines)) #문단 수 : 6
    #(4) readline():한 줄 읽기
    test = open('pywork/test.txt', mode = 'r')
    line = test.readline() #한 줄 읽기
    print(line)
    print(type(line)) #<class 'list'>
except Exception as e:
    print('Error 발생 :', e)
finally:
    #파일 객체 닫기
    test.close()