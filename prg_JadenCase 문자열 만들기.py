# split(), split(' ') 는 다르다
# " adgagd 3eagdag " -> " Adgagd 3eagdag " 인 경우, 공백 모두 포함해야한다.

def solution(s):
    answer =''
    flag = 'start'
    for i in s:
        if i == ' ':
            answer += ' '
            flag = 'start'
            
        elif flag == 'start' and i.isalpha():
            answer += i.upper()
            flag = 'no'
            
        else:
            answer += i.lower()
            if flag == 'start':
                flag = 'no'
                
    return answer
