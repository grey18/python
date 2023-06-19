'''bulitins 모듈에 있는 함수는 내장함수이기에 별다른 명령어 없이 함수 사용가능
But 다른 함수를 사용하기 위해서는 다음과 같은 형식으로 모듈을 포함해야 함
형식1) import 모듈명
형식2) from 모듈명 import 함수명1, 함수명2...'''

#(1) builtins 함수
help(len)
dataset = list(range(1,6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

#(2) import 함수
import statistics #방법 1
from statistics import variance, stdev #방법 2

print('평균=', statistics.mean(dataset)) #방법 1
print('중위수=', statistics.median(dataset)) #방법 1
print("표준 분산=", variance(dataset)) #방법 2
print("표본 표준편차=", stdev(dataset)) #방법 2