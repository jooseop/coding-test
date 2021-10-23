# solution1
def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)
        
def solution(arr):
    answer = arr[0]
    if len(arr) > 1:
        for a in arr[1:]:
            answer = lcm(answer, a)
            
    return answer


# solution2
def solution(arr):
    # 소수
    n = max(arr)
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 1/2) + 1):
        if sieve[i] == True:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    sieve = [idx for idx, val in enumerate(sieve) if val == True]
    
    # 소수, 곱 횟수
    d = {i : 0 for i in sieve} 

    for a in arr:
        for s in sieve:
            if a >= s:
                count = 0

                while a > 1:
                    if a % s == 0:
                        a = a // s
                        count += 1
                    else:
                        break

                if d[s] < count:
                    d[s] = count

    answer = 1
    for key, value in d.items():
        if value > 0:
            answer *= (key ** value)

    return answer
