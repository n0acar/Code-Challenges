import numpy as np
from itertools import product
import sys

nList=[]
dietList=[]
indexR=0
for i in sys.stdin:
    indexC=0
    ab=i.split()
    if indexR==0:
        n=int(ab[0])
    else:
        if indexC==0:
            nDiet = int(ab[0])
            nList.append(nDiet)
            indexC+=1
        diet=[]
        if nDiet!=0:
            for a in range(nDiet):
                diet.append(int(ab[a+1]))
        dietList.append(diet)    
    indexR+=1
    if indexR==n+1:
        break
binaryList=[]
lst = list(product([0, 1], repeat=sum(nList)))    
for i in range(len(lst)):
    zeros=np.zeros((n,n))
    index=0
    for j,diet in enumerate(dietList):
        if diet!=[]:
            for d in diet:
                zeros[j][d-1]=lst[i][index]
                index+=1
    binaryList.append(zeros)

sum=0
for binaryMatrix in binaryList:
    counter=0
    distanceListClock=[]
    distanceListCounter=[]
    for i, item in enumerate(binaryMatrix):
        for j, it in enumerate(item):
            if it == 1:
                counter+=1
                dif=abs(j-i)
                if j-i>0:
                    distanceListClock.append(dif)
                    distanceListCounter.append(n-dif)
                elif j-i==0:
                    distanceListClock.append(0)
                    distanceListCounter.append(0)
                else:
                    distanceListClock.append(n-dif)
                    distanceListCounter.append(dif)
                    
            
    if counter!=0:
        maxCounter=max(distanceListCounter) 
        maxClock=max(distanceListClock)
        if maxCounter>maxClock:
            sum+=maxClock
        else:
            sum+=maxCounter

print(sum%1000000009)



