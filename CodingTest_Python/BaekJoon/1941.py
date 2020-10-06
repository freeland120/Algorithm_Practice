#flood fill 알고리즘



def recur(x,y,cnt):
    if cnt == 7:
        print(arr)
        return
    
    if y == 5:
        x += 1
        y = 0
    
    if x == 5:
        return
    
    arr.append([x,y])
    recur(x,y+1,cnt+1)
    arr.pop()
    recur(x,y+1,cnt)

arr = []

#for i in range(5):
    #arr.append(input()) 



recur(0,0,0)