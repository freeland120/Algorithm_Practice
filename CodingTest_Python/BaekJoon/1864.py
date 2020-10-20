


def solution(x):

    result = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}.get(x,10)

    return result



data = []


while True:
    n = input()
    if n == "#":
        break

    
    ans = 0
    for i in range(1,len(n)+1):
        A = solution(n[i-1])
        ans += A * pow(8,len(n)-i)
    data.append(ans)


for i in data:
    print(i)

   
