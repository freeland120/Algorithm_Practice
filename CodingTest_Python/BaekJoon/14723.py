


n = int(input())

f = 0

for i in range(1,100):
    if n <= k:
        if n % i:
            (k-n) % i+1
        else:
            print(1)
        
        if n % i:
            n % i
        else:
            print(f)



f-n %i+1 if n%i else 1, n%i if n%i else f
