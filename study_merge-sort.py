def merge(num, low, mid, high):
    tmp = []
    i, j = low, mid + 1
    
    while i <= mid and j <= high:
        if num[i] < num[j]:
            tmp.append(num[i])
            i += 1
        else:
            tmp.append(num[j])
            j += 1
        
    if i <= mid:
        tmp += num[i : mid + 1]
    else:
        tmp += num[j : high + 1]
    
    for k in range(low, high + 1):
        num[k] = tmp[k - low]
    
    return num


def merge_sort(num, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(num, low, mid)
        merge_sort(num, mid + 1, high)
        return merge(num, low, mid, high)

    
n = int(input())
num = list(map(int, input().split()))
answer = merge_sort(num, 0, n - 1)
for i in answer:
    print(i, end=' ')
