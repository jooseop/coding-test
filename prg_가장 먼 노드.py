from collections import deque
def solution(n, edge):
    aj = {i : [] for i in range(1, n + 1)}
    check = [0] * (n+1)
    
    for a, b in edge:
        aj[a].append(b)
        aj[b].append(a)
    
    queue = deque([1])
    check[1] = 1 # 여기를 체크해줘야 함, 안하면 역으로 돌아올 수 있음
    
    while queue:
        pop = queue.popleft()
        
        for i in aj[pop]:
            if check[i] == 0: # 아직 거치지 않았으면
                check[i] = check[pop] + 1 # 지금까지 거쳐온 거리 + 1
                queue.append(i)
                

    return check.count(max(check))
