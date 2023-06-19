'''
재귀함수
카운트
'''

#(1) 재귀함수 정의:1~n 카운트
def Counter(n):
    if n == 0:
        return 0 #종료 조건
    else:
        Counter(n-1) #재귀 호출

#(2) 함수 호출1
print('n=0:', Counter(0))

#(3) 함수 호출2
Counter(5)

#(1) 재귀함수 정의:1~n 누적합(1+2+3+4+5=15)
def Adder(n):
    if n == 1: #종료 조건
        return 1
    else:
        result = n + Adder(n-1) #재귀 호출
        print(n, end=' ') #(4) 스택 영역: 2 3 4 5
        return result
    
#(2) 함수 호출1
print('n=1:', Adder(1))

#(3) 함수 호출2
print('\nn=5:', Adder(5))