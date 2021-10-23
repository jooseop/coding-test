from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    
    while people:
        rm1 = limit - people.pop()
        if people and rm1 > 0 and rm1 - people[0] >= 0:
            people.popleft()
        answer += 1
    return answer

'''
- 탐욕법(그리디)
- 조건 : 최대 2명까지 탐
- 풀이 : 가장 무거운 사람 1명, 여유 있으면 가장 가벼운 사람 1명
'''
