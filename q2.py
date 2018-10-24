import sys
rowList=[]
columnList=[]
index=0
for i in sys.stdin:
    if index==0:
        ab=i.split()
        m=int(ab[0])
        n=int(ab[1])
    elif index==1:
        ab=i.split()
        for a in range(m):
            rowList.append(int(ab[a]))
    elif index==2: 
        ab=i.split()
        for a in range(n):
            columnList.append(int(ab[a]))
    index+=1
    if index==3:
        break
if m<n:
    temp=m
    m=n
    n=temp
    temp=rowList
    rowList=columnList
    columnList=temp
maxRow=max(rowList)
maxColumn=max(columnList)
row0=rowList.count(0)
column0=columnList.count(0)
for i in range(row0):
    rowList.remove(0)
for i in range(column0):
    columnList.remove(0)
sortedColumnList=sorted(columnList, reverse=True)

def recursiveCheck(rowList, sortedColumnList):
    if len(rowList)==0:
        return sortedColumnList
    sub=rowList.pop()
    for i in range(sub):
        sortedColumnList[i]-=1
    sortedColumnList=sorted(sortedColumnList, reverse=True)
    return recursiveCheck(rowList, sortedColumnList)
if m-row0<maxColumn or n-column0<maxRow:
    print("No")
else:
    if any(recursiveCheck(rowList, sortedColumnList)):
        print("No")
    else:
        print("Yes")
