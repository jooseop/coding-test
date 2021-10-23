# solution1
'''
citations = [3, 0, 6, 1, 5]
1. sort -> 6 5 3 1 0

2. enumerate(citations, start=1)
    -> list : [(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)]
    -> index는 citations에서 자신의 val 이상의 개수가 된다.

3. map(min, enumerate(citations, start=1))
    -> list : [1, 2, 3, 1, 0]

4. max(map)
'''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
    
   
# solution2
def solution(citations):
    h = 0
    for i in range(max(citations)):       
        many, little = 0, 0
        for c in citations:
            if c >= i:
                many += 1
            if c <= i:
                little += 1
        if many >= i and little <= i:
            h = i
    return h
