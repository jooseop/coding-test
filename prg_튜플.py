'''
{{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
(a1, a2, a3, ..., an)
-> 많이 나온 순서대로 정렬

from collections import Counter
'''

from collections import Counter
def solution(s):
    s = list(map(int, s.replace('{', '').replace('}', '').split(',')))
    answer = [i[0] for i in sorted([(key, val) for key, val in Counter(s).items()], key=lambda x: x[1], reverse=True)]
    return answer
