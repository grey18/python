'''
반복문(for)
형식) 
for 변수 in 열거형 data
    실행문
    실행문

제너레이터식 : 변수 in 열거형data(object)
열거형data(iterable) : string, list, tuple. set, dict
'''

#문자열 열거형객체 이용
string = "홍길동"

#1문자 -> 변수 넘김 : 3회
print(len(string)) # 3

for s in string:
    print(s)

print() # line skip

# split -> 변수 넘김 : 3회
for s in string.split(): # sep=' '
    print(s, end=' ')

print()

#list 열거형객체 이용
lstset = [1,2,3,4,5] #1차원(vector)

for e in lstset:
    print('원소 : ', e)

help(range)

'''
range(stop) : 0~stop-1 정수
range(start, stop) : start-stop-1 정수
range(start, stop, stop) : start~stop, stop 단위 증감
''' 

num1 = range(10) #0~4
print('num1 : ', num1) # range(0, 10)

num2 = range(1, 10)
print('num2 : ', num2) # range(1, 10)

num3 = range(1, 10, 2)
print('num3 : ', num3) #range(1, 10, 2)

for n in num1:
    print(n, end=' ')

print()

for n in num2:
    print(n, end=' ')

print()

for n in num3:
    print(n, end=' ')

num2 = range(1,5) #1~4
print('num2 : ', num2) # num2 : range(1,5)

num2 = list(num2)
print(num2) # [1, 2, 3, 4]

#lst(1~100) 중에서 3의 배수만 lst3 추가/출력
lst = list(range(3, 101, 3)) #1~100
print('lst:', lst)

#중첩 반복문
#구구단 출력(2, 3, 5)
for i in [2, 3, 5]:
    #바깥쪽 영역
    print('~~~ {}단 ~~~'.format(i))
    for j in range(1,10):
        #안쪽 영역
        print('%d * %d = %d' %(i, j, i * j))

string = '''나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다.'''

sents = [] #문장 저장
words = [] #단어 저장

for sen in string.split(sep ="\n"): #문단 -> 문장
    sents.append(sen)
    for word in sen.split(): #문장 -> 단어
        words.append(word)

print('문장 :', sents)
print('문장수 :', len(sents))
print('단어 :', words)
print('단어수 :', len(words))