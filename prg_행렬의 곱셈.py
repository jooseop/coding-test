# solution1
def solution(arr1, arr2):
    return [[ sum(i * j for i, j in zip(a1, a2)) for a2 in zip(*arr2)] for a1 in arr1]


# solution2
def solution(arr1, arr2):
    answer = []
    for a1 in arr1:
        row = []
        for a2 in zip(*arr2):
            tmp = 0
            for i, j in zip(a1, a2):
                tmp += i * j
            row.append(tmp)
        answer.append(row)
    return answer
