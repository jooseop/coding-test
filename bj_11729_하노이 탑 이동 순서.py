def hanoi(start, end, via, n):
    global count, answer
    if n == 1:
        count += 1
        answer.append(str(start) + " " + str(end))
        return
    
    hanoi(start, via, end, n - 1)
    count += 1
    answer.append(str(start) + " " + str(end))
    hanoi(via, end, start, n - 1)


n = int(input())
count = 0
answer = []
hanoi(1, 3, 2, n)
print(count)
for i in answer:
    print(i)
