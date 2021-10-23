# 수가 나올 때마다 찾지 않고, 최대 수를 통해 소수 리스트를 만들어 리스트 값만 비교 (시간복잡도 줄이기)

from itertools import permutations
def solution(numbers):
    answer = 0

    # 순열
    num = set(int(''.join(pm))  for l in range(1, len(numbers) + 1) for pm in permutations(numbers, l))
    
    # 가장 큰 수로 소수 리스트 만들기
    n = max(num)
    sieve = [False, False] + [True] * (n - 1)
    
    for i in range(2, int(n ** 1/2) + 1):
        if sieve[i] == True:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    
    # 순열 중에서 소수
    for i in num:
        if sieve[i] == True:
            answer += 1
    
    return answer
