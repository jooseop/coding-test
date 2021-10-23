def solution(weights, head2head):
    # 승률
    win = [ ]
    for h2h in head2head:
        total = h2h.count('W') + h2h.count('L') 
        if total == 0:
            win.append(0)
        else:
            win.append(h2h.count('W') / total)
    
    # 무거운 복서
    over = [0] * len(weights)
    for head_idx, head in enumerate(head2head):
        for h_idx, h in enumerate(head):
            if h == 'W' and weights[head_idx] < weights[h_idx]:
                over[head_idx] += 1
    
    # 인덱스 + 1, 승률, 무거운복서승, 무게
    l = [(idx + 1, val[0], val[1], weights[idx]) for idx, val in enumerate(zip(win, over))]
    l.sort(key = lambda x : (-x[1], -x[2], -x[3], x[0]))
    
    return [i[0] for i in l]
