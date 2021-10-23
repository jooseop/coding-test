# 팰린드롬이 아니면 답은 1이다.
def solution(s):
    answer = 1

    for i in range(len(s)):    
        for j in range(i):    
            
            if s[j:i+1] == s[i+1:i+1 + i - j + 1][::-1]:
                if answer <= (i - j + 1) * 2:
                    answer = (i - j + 1) * 2
                    
            if s[j:i] == s[i+1:i+1 + i-j][::-1]:
                if answer <= (i - j) * 2 + 1:
                    answer = (i - j) * 2 + 1

    return answer
