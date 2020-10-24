#애너그램 만들기

#1.입력받은 문자열에서 알파벳이 몇개 있는 확인

#0으로 초기화
a = [0]*26
b = [0]*26

cnt = 0


a_gram = list(input())
b_gram = list(input())

for i in range(0,len(a_gram)):
    #ord()내장함수를 사용해 문자를 '아스키 코드값'으로 바꿔주자
    a[ord(a_gram[i]) - 97] += 1

for i in range(0,len(b_gram)):
    b[ord(b_gram[i]) - 97] += 1

#서로 개수가 다를 경우 갯수 차이의 절대값을 cnt에 더해준다.
for i in range(0,26):
    if a[i] != b[i]:
        cnt += abs(a[i]-b[i])

print(cnt)