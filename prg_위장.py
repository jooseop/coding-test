from collections import defaultdict
def solution(clothes):
    d = dict()
    for name, kind in clothes:
        if kind not in d:
            d[kind] = 1
        else:
            d[kind] += 1
    
    tmp = 1
    for key, value in d.items():
        tmp *= (value + 1)
    
    return tmp - 1
