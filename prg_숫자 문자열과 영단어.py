# replace는 변수에 할당해줘야지 바뀜, 원본값에 할당 안됨
# 정규식 import re, re.findall


# solution 1
def solution(s):
    d = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', 'zero' : '0'}
    for key, value in d.items():
        s = s.replace(key, value)
    return int(s)


# solution 2
import re
def solution(s): 
    answer = ''
    d = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', 'zero' : '0'}
    re_s = re.findall('one|two|three|four|five|six|seven|eight|nine|zero|[0-9]', s)
    for i in re_s:
        if i in d:
            answer += d[i]
        else:
            answer += i
    return int(answer)
