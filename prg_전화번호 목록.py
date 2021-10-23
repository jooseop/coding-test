# 정확성 : 접두어인 경우 찾기, {11, 2211} 인 경우는 걸러야 한다.
# 효율성 : for 2번은 전체 비교, 효율성 떨어짐 -> for 1번, 정렬된 상태에서 양 옆을 비교하기
# https://blog.naver.com/azprncs/222455398621

def solution(phone_book):        
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            return False
    else:
        return True
