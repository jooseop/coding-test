def solution(n):
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return b % 1000000007

# 파이썬 - 다중할당 (파이썬 알고리즘 인터뷰 p.211~212]
# -> 뒤애 있는 값을 앞 변수에 넣어줌
# 풀이 : https://wwlee94.github.io/category/algorithm/dp/2xn-tiling/
