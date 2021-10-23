answer = 0
count = 0
nums = []


def dfs(target):
    global count, answer
    tmp = ''.join(str(i) for i in nums)
    if tmp == target:
        answer = count
        return
        
    count += 1
    if len(nums) == 5:
        return

    for i in range(1, 6):
        nums.append(i)
        dfs(target)
        nums.pop()


def solution(word):
    vowel = {'A':1, 'E':2, "I":3, "O":4, "U":5}
    target = ''
    for w in word:
        target += str(vowel[w])
        
    dfs(target)
    return answer
