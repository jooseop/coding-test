n = int(input())
l = list(set([input() for _ in range(n)]))
l.sort(key=lambda x : ((len(x), x)))

for i in l:
    print(i)
