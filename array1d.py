array1 = [1,1,0,1,1,1,1,0,1,1]

array0 = []
totalOnes = 0

for i in array1:
    if i:
        totalOnes +=1 
    elif i == 0:
        array0.append(totalOnes)
        totalOnes = 0
        array0.append(0)

if array1[-1] == 1:
    array0.append(totalOnes)

print(array0)

maxSeq = []
arr2 = 0
for i in array0:
    if i+2 < len(array0):
        arr2 = array0[i]+array0[i+2]
        maxSeq.append(arr2)
        arr2 = 0

print("the maximum sequence could be is {} ".format(max(maxSeq)+1))

