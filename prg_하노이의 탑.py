def hanoi(n, start, end, sub, answer):    
    # 1st. 원반개수 한개일때를 작성
    if n == 1:
        answer.append([start, end])
        return

    # 2nd. 가장 큰 원반 빼고 나머지는 보조기둥으로 옮긴다.
    hanoi(n - 1, start, sub, end, answer)
    # >>> 이 작업을 수행할 때, 아래의 큰 원반은 없고 진행한다고 생각해보기
    # 여기에서는 원반개수가 1이 될때까지, 이 다음의 작업은 수행하지 않는다.
    
    answer.append([start, end])
    
    # 3rd. 가장 큰 원반이 목표로 갔다면, 나머지 원반은 보조기둥이 시작점이고, end를 목표로 옮기면 된다.
    hanoi(n - 1, sub, end, start, answer)
    
    
def solution(n):
    answer = []
    # 하노이 시작 : (개수, 시작, 목표, 도착)
    hanoi(n, 1, 3, 2, answer)
    return answer
