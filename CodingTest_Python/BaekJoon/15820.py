


s1,s2 = map(int,input().split())



test_case = True

for _ in range(s1):
    a,b = map(int,input().split())
    if a != b:
        test_case = False


sample_case = True

for _ in range(s2):
    a,b = map(int,input().split())
    if a != b:
        sample_case = False


if sample_case and test_case:
    print("Accepted")
elif not sample_case and test_case:
    print("Why Wrong!!!")
else:
    print("Wrong Answer")










