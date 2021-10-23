def solution(s):
    count, zero = 0, 0

    while s != '1':
        count += 1
        zero_remove, s = s.count('0'), s.replace('0', '')
        zero += zero_remove
        s = str(bin(len(s))[2:])
        
    return count, zero
