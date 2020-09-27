## Hasy-key 위장


def solution(clothes):
    cloth = {}

    for i in clothes:
        cloth[i[1]] = cloth.get(i[1],0) + 1
    
    value = list(cloth.values())

    #전체 - 모두 안입을 때
    #전체 ex) 상의 a,b가 있을 때 경우는 0안입음, a입음, b안입음

    m = 1

    for v in value:
        m *= (v+1)
    
    return m - 1


# def solution(clothes):
#     answer = {}

#     for i in clothes:
#         if i[1] in answer: 
#             answer[i[1]] += 1
#         else:
#             answer[i[1]] = 1
        
#     count = 1

#     for i in answer.values():
#         count *= (i+1)
#     return count - 1




# years = {'a': 2012, 'b':2013, 'c':2020}


# result = years.get('c', 'Nothing')

# print(result)






# def solution(clothes):

#     answer = 1
#     cloth = {}

#     for i in clothes:
#         cloth[i[1]] = 1

#     for i in clothes:
#         cloth[i[1]] += 1

#     for i in cloth.values():
#         answer *= i
    
#     answer -= 1

#     return answer















