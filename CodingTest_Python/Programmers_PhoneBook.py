# 전화번호 목록


##이중 for문 이용해서 한것

# def solution(phone_book):
#     #phone_book.sort()
    
#     for a in range(len(phone_book)):
#         k1 = len(phone_book[a])
        
#         for b in range(a+1,len(phone_book)):
#             k2 = len(phone_book[b])

#             if phone_book[a] in phone_book[b][:k1] or phone_book[b] in phone_book[a][:k2] :
#                 return False
#     return True

#//////////////////////////////////////////


## sort()이용한 풀이

# def solution(phone_book):

#     phone_book.sort()

#     for i in range(len(phone_book)-1):
#         if phone_book[i] in phone_book[i+1]:
#             return False
#     return True

## startswith() 이용한 풀이   //find(찾을문자, 찾기시작할위치) // startswith(시작하는문자, 시작지점) // endswith(끝나는문자, 문자열의시작, 문자열의끝)

# def solution(phone_book):
#     phone_book.sort()
#     print(phone_book)
#     for a, b in zip(phone_book,phone_book[1:]):
#        if b.startswith(a):
#            return False
#     return True
    

# list1 = ["119", "97674223", "1195524421"]
# list2 = ["123", "456", "789","12332334132"]


# print(solution(list2))



