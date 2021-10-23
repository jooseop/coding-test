n = int(input())
num = sorted(list(map(int, input().split())))
x = int(input())

l, r = 0, len(num) - 1
answer = 0
while l < r:
    sum_num = num[l] + num[r]
    if x == sum_num:
        answer += 1
        l += 1 # or r -= 1

    if x > sum_num:
        l += 1

    if x < sum_num:
        r -= 1

print(answer)
