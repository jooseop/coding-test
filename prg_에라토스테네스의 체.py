'''
제곱근까지만 구하는 이유 : 어떤수의 약수는 대칭의 형태이다. 예를 들어, (1, 2, 4, 8, 16) 2에서 8을 찾을 수 있다.
for(2~n의 제곱근) -> if(소수이면)(가지치기) -> for(그 수의 배수는 소수가 아니다)
'''

'''
n ** 1/2 = n / 2
n ** (1/2) = n ** 0.5
서로 다름
'''

# !solution
def solution(n):
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** (0.5)) + 1):
        if sieve[i] == True:
            for j in (i * 2, n + 1, i):
                sieve[j] = False
    return [idx for idx, val in enumerate(sieve) if val]

# solution1
def erathos(n):
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        sieve[i * 2::i] = [False] * ((n - i) // i) # 배수부분 체크
    return [idx for idx, val in enumerate(sieve) if val]

# solution2
def get_primes(n):
    is_prime = [False, False] + [True] * (n - 2)

    for i in range(int(n // 2) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i): # 제곱이 되는 수부터 체크
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]
