def solution(n):
    l = [0, 1]

    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    
    return l[n] % 1234567
  
# 1234567로 나누는 이유 : https://programmers.co.kr/questions/11991
