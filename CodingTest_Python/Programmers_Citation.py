## 정렬 "H-index"문제



def solution(citations):
    citations.sort()

    l = len(citations)
    
    for i in range(l):
        if citations[i] >= l-i:
        # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l - i
    return 0



citations = [3,0,6,1,6]

print(solution(citations))