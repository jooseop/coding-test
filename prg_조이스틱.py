# https://bellog.tistory.com/152
def solution(name):
    updown = 0
    min_move = len(name) - 1
    
    # 상하 : N 기준
    for idx, val in enumerate(name):
        ord_val = ord(val)
        if ord_val > 78:
            updown += 91 - ord_val
        else:
            updown += ord_val - 65
        
        # 좌우
        '''
        1. 한방향(왼쪽)으로만 이동하는 방법 : min_move = len(name) - 1
        2. 중간에 A가 나와서 되돌아 가는 경우
        -> 왼쪽에서 현재까지 이동한 index * 2 + (전체길이 - 연속되는 마지막 A의 위치 전까지)
        -> A가 나오고, 계속 A가 있으면 while문으로 next_idx += 1
        '''
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, idx + idx + len(name) - next_idx)
        
    return updown + min_move
