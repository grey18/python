'''
파일 시스템
os 모듈의 파일과 디렉터리 관련 함수
'''

import os.path #window 파일 경로를 조작하는 모듈

#현재 경로 확인
os.getcwd()
#경로 변경
os.chdir('변경할 디렉터리')
#디렉토리와 파일의 절대경로
os.path.abspath('파일명')
#파일의 디렉터리 이름
os.path.dirname('파일명')
#디렉터리 유무 확인
os.path.exists('디렉터리 주소')
os.path.isdir('디렉터리명')
#파일 유무 확인
os.path.isfile('파일명')
#디렉터리와 파일 분리
os.path.split('파일 주소')
#디렉터리와 파일 결합
os.path.join('디렉터리 주소와 파일명')
#파일 크기
os.path.getsize('디렉터리/파일명')

'''
glob 모듈
'''

import glob

glob.glob('test*.py') #현재 경로에서 test로 시작하는 모든 목록 반환
glob.glob('c:/test[0-9]') #test 문자열 다음에 숫자 1개가 오는 목록 반환 ['c:/test1', 'c:/test9']
glob.glob('c:/test[0-9]/*.txt') #test1, test9 디렉터리에 포함된 *.txt 파일 반환
glob.glob('c:/test[0-9]/[0-9].*') #test1, test9 디렉터리에서 숫자 1개 파일 반환
glob.glob('c:/test1/*.txt') #test1 디렉터리에서 *.txt 파일 반환
glob.glob('c:/test1/*.txt', recursive=True) # *.txt파일을 내림차순 정렬하여 반환