def solution(sizes):
    sizes.sort(key=lambda x: max(x), reverse=True)
    w, h = max(sizes[0]), min(sizes[0])
    
    for i, j in sizes[1:]:
        if min(i, j) > h:
            h = min(i, j)
    
    return w * h
