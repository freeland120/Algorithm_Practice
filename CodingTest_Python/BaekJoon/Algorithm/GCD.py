



#유클리드 호제법
#두 자연수 A,B에 대하여(A>B) A를 B로 나눈 나머지 R이라고 할때,
#이 때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

def GCD(a,b):
    if a % b == 0:
        return b
    
    result = GCD(b, a % b)

    return result



A,B = map(int,input().split())

print(GCD(A,B))