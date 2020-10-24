
#저항문제
#데이터 크기가 커지면 시간이 오래 걸림...
def solution(a,b,c):

    ret = int(str(a)+str(b))*(10 ** c)

    return ret


color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']



first = color.index(input())
second = color.index(input())
third = color.index(input())


ans = solution(first,second,third)


print(ans)