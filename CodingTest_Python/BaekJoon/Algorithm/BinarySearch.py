

def binsearch(n,S,x):
    low = 1
    high = n
    location = 0

    while (low <= high and location == 0):
        mid = (low+high) // 2
        if x == S[mid]:
            location == mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return location



target = int(input())
S = [-123,123,423,454,642,871,999,1000,1024,1045]

result = binsearch(len(S)- 1,S,target)

print(result)