#Solving facebook interview task "Spiral Matrix"
from typing import Any


def mySpiral(mylist=[],*args):
    theSpiral = []
    top = mylist[0]
    bot = []
    left = []
    right = []
    mid = []
    tempMid = []
    #right
    for i in range (len(mylist)):
        i += 1
        try:
            leftItem = mylist[i][-1]
            left.append(leftItem)
        except IndexError:
            continue

    #bot
    i = mylist[-1] #3
    for i in range (len(mylist)):
        if i >0 and i < len(mylist) -1:
            try:
                rBot = mylist[-1][i]
                bot.append(rBot)
            except IndexError:
                continue
    

    #left
    for i in range (len(mylist)):
        i += 1
        try:
            rightItem = mylist[i][0]
            right.append(rightItem)
        except IndexError:
            continue
    

    #mid
    if len(mylist) < 4 :
        for i in range (len(mylist)):
            i +=1
            if i > 0 and i < len(mylist) -1 :
                try:
                    midItem = mylist[1][i]
                    mid.append(midItem)
                except IndexError:
                    continue    
    else:
        for i in range (len(mylist)):
            i +=1
            if i > 0 and i < len(mylist) -1 :
                try:
                    midItem = mylist[1][i]
                    mid.append(midItem)
                except IndexError:
                    continue    
        for i in range (len(mylist)):
            
            i +=1
            if i > 0 and i < len(mylist) -1 :
                try:
                    midItem = mylist[2][i]
                    tempMid.append(midItem)
                except IndexError:
                    continue        
            tempMid.reverse()
        
 
    


    right.reverse()
    bot.reverse()
    
    print(tempMid)
    print(top,left,bot,right,mid,tempMid)
    
    
    for i in top:
        theSpiral.append(i)
    for l in left:
        theSpiral.append(l)
    for b in bot:
        theSpiral.append(b)
    for r in right:
        theSpiral.append(r)
    for m in mid:
        theSpiral.append(m)
    for t in tempMid:
        theSpiral.append(t) 

    for i in theSpiral:
        print(i)


array1 = [[1,2,3,0],
         [4,5,6,1],
         [7,8,9,2],
         [1,2,3,4]]
mySpiral(array1)
