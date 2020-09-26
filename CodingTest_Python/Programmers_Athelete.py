#완주하지 못한 선수

# def solution(participant,completion):
    
#     participant.sort()
#     completion.sort()
#     print(participant)
#     print(completion)

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]

#     return participant[i+1]

## collections.Counter를 이용한 카운팅 방법
# from collections import Counter

# def solution(participant,completion):

#     participant.sort()
#     completion.sort()

#     result = Counter(participant) - Counter(completion)
    
#     return list(result.keys())[0]




# list1 = ["mislav", "stanko", "mislav", "ana","ydg","mislav"]
# list2 = ["stanko", "ana", "mislav"]


# print(solution(list1,list2))





# list1 = ["mislav", "stanko", "mislav", "ana"]
# list2 = ["stanko", "ana", "mislav"]



# print(solution(list1,list2))


#dictionary를 이용한 카운팅
#아래코드는 어떤 단어가 주어졌을 때 단어에 포함된 각 알파벳의 글자 수를 세어주는 간단한 함수입니다.


# def countLetters(word):
#     counter = {}

#     for letter in word:
#         if letter not in counter:
#             counter[letter] = 0
#         counter[letter] += 1
#     return counter



# print(countLetters('hello world'))


# from collections import Counter

# result = Counter("hello World")

# print(result)




# from collections import Counter

# result = Counter("hello world").most_common(3)

# print(result)



