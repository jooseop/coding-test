def count(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    return s

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        c = count(i)
        print(c)
        if c % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
  
# 제곱수는 약수의 개수가 홀수개인 것을 이용하여 해결한 코드도 있음
