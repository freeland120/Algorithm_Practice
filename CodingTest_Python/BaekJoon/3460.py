


#이진수
#bin(),oct(),hex()

Test_Case = int(input())


for _ in range(Test_Case):

    n = bin(int(input()))[2:]
    print(type(n))
    for i in range(len(n)):
        if n[-1-i] == "1":
            print(i,end=" ")
    print()


