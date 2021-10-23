def solution(n):
    answer = 0
    
    for start in range(1, n + 1):
        tmp = 0

        while tmp < n:
            tmp += start
            start += 1
            
            if tmp == n:
                answer += 1
                break
        
    return answer
