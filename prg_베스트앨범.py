def solution(genres, plays):
    # 장르 딕셔너리
    d = dict()
    for g, p in zip(genres, plays):    
        if g in d.keys():
            d[g] += p
        else:
            d[g] = p
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    # 장르별, plays의 (인덱스, 재생횟수)
    l = [[(idx, p) for idx, (g, p) in enumerate(zip(genres, plays)) if g == i[0]] for i in d]

    # 장르 - 재생횟수 - 고유번호, 최대 2개
    return [first[0] for i in l for first in sorted(i, key=lambda x: (-x[1], x[0]))[:2]]
