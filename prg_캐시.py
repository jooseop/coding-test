# deque([,maxlen])
from collections import deque
def solution(cacheSize, cities):
    time = 0
    cache = deque()
    # cache = deque(maxlen=cacheSize)
    
    # 1. deque(maxlen=cacheSize) -> if문 없어도 됨
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            # 2. deque(maxlen=cacheSize) -> if문 없어도 됨
            if len(cache) >= cacheSize:
                cache.popleft()
            
            cache.append(city)

    return time
