def solution(N, stages):
    s = [stages.count(i) for i in range(1, N + 1)]

    pb = []
    for i in range(len(s)):
        if sum(s[i:]) == 0:
            pb.append((i+1, 0))
        else:
            pb.append((i + 1, s[i] / (sum(s[i:]) + len(stages) - sum(s))))
            
    pb.sort(reverse=True, key=lambda x : (x[1], -x[0]))
    answer = [i[0] for i in pb]
    return answer
