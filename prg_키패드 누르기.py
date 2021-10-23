def solution(numbers, hand):
    board = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    l, r = (3, 0), (3, 2)
    p = ''
    
    for n in numbers:
        if n in {1, 4, 7}:
            l = (board[0].index(n), 0)
            p += 'L'

        elif n in {3, 6, 9}:
            r = (board[2].index(n), 2)
            p += 'R'
            
        else:
            n = (board[1].index(n), 1)
            nl = abs(l[0] - n[0]) + abs(l[1] - n[1])
            nr = abs(n[0] - r[0]) + abs(n[1] - r[1])

            if nl < nr:
                l = n
                p += 'L'
            elif nl > nr:
                r = n
                p += 'R'
            else:
                if hand == "left":
                    l = n
                    p += 'L'
                else:
                    r = n
                    p += 'R'
    return p
