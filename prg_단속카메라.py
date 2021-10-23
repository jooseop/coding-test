def solution(routes):
    l, r = -30000, 30000
    answer = 0
    
    for r0, r1 in sorted(routes):
        if r < r0:
            answer += 1       
            l, r = r0, r1
        else:
            if l < r0:
                l = r0
            if r1 < r:  
                r = r1
    answer += 1

    return answer
