# python 정렬: center, ljust, rjust, zfill

def solution(n, arr1, arr2):
    board = []
    for i1, i2 in zip(arr1, arr2):
        tmp = ''
        for _ in range(n):
            decode = str((i1 % 2) | (i2 % 2))
            i1, i2 = i1 // 2, i2 // 2
            tmp = decode + tmp
        board.append(tmp.replace('1','#').replace('0',' '))
    return board
