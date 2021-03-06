'''
"나보다 체력이 낮은 캐릭터가 쓸 수 있는 아이템은 나도 쓸 수 있다 https://racoon-blue.tistory.com/10"

1. 체력 낮은 캐릭터 순서 탐색 // 체력순 정렬 : O(n log n)
2. 체력을 낮추는 아이템이 낮은 아이템 순서로 탐색 // 체력이 높은 캐릭터는 그 아이템을 당연히 쓸 수 있음
3. 통과하는 아이템들을 따로 모음
4. 따로 모은 아이템들 중에서 공격력이 가장 센 것을 사용 // o(1)
5. 아이템을 사용했으면 아이템을 삭제해주자 // O(1) // 1로 처리해주기 위해 deque 사용
'''

'''
# deque mutated during iteration
-> for 안에서 pop을 하면, deque가 변경되었다고 나옴
-> while을 써야 함
'''

from heapq import heapify, heappush, heappop
from collections import deque
def solution(healths, items):
    answer = []
    heap = []

    healths.sort() # 체력 오름차순 정렬 // O(N log N)
    items = deque(sorted([(item[1], item[0], index + 1) for index, item in enumerate(items)])) # 낮추는 체력, 높이는 공격치, 인덱스 // enumerate, list comprehension
    
    for health in healths: # 제일 낮은 체력부터 루프
        
        while items: # 아이템 루프
            debuff, buff, index = items[0] # 있는 아이템중 가장 낮추는 체력이 낮은 아이템
            
            if health - debuff < 100: # 체력을 낮췄는데 100보다 작음
                break # 루프 종료
            
            # 체력 조건을 통과한 경우
            items.popleft() # 아이템 사용했으니까 없애줌 // 어차피 다음 체력에서는 무조건 가능하고, 만약 지금 당장 item을 안쓰더라도 heap에 있기 때문에 다음에 아이템을 사용할 수 있다.
            heappush(heap, (-buff, index)) # 힙에 사용한 버프랑, 인덱스번호를 max heap 기준으로 넣어줌, 여러가지 item이 들어가면 공격력이 강한 순으로 정렬됨 // O(log N)
            
        if heap: # heap에 아이템이 있으면
            _, index = heappop(heap) # 공격력 최대인 것을 pop
            answer.append(index)

    return sorted(answer)
