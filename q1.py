import sys
letterList=["A", "B", "C", "D", "E", "F", "G", "H"]
numberList=[1, 2, 3, 4, 5, 6, 7, 8]
def printForOneLine(sLetter, sNumber, fLetter, fNumber):
    printStr=''
    count=0
    letterSign=1
    numberSign=1

    flag=True

    tLetterIndex=letterList.index(fLetter)
    tNumberIndex=numberList.index(fNumber)

    letterIndex=letterList.index(sLetter)
    numberIndex=numberList.index(sNumber)


    letterDif=letterIndex-tLetterIndex
    numberDif=numberIndex-tNumberIndex

    if (numberDif-letterDif)%2==1:
        return 'Impossible'

    if letterIndex>tLetterIndex:
        letterSign=-1
    else:
        letterSign=1
    if numberIndex>tNumberIndex:
        numberSign=-1
    else:
        numberSign=1
    if letterIndex==7:
        letterSign=-1
    if numberIndex==0:
        numberSign=1
    if numberIndex==7:
        numberSign=-1
    if letterIndex==0:
        letterSign=1
    printStr+=' '
    printStr+=letterList[letterIndex]
    printStr+=' '
    printStr+=str(numberList[numberIndex])
    while abs(letterDif)!=abs(numberDif):
        letterIndex+=letterSign
        numberIndex+=numberSign
    
        letterDif=letterIndex-tLetterIndex
        numberDif=numberIndex-tNumberIndex 
    
        if letterIndex==0 or letterIndex==7:
            letterSign*=-1
            printStr+=' '
            printStr+=letterList[letterIndex]
            printStr+=' '
            printStr+=str(numberList[numberIndex])
            count+=1
            if abs(letterDif)==abs(numberDif):
                flag=False
        if numberIndex==0 or numberIndex==7:
            numberSign*=-1
            printStr+=' '
            printStr+=letterList[letterIndex]
            printStr+=' '
            printStr+=str(numberList[numberIndex])
            count+=1
            if abs(letterDif)==abs(numberDif):
                flag=False
    
        if flag and abs(letterDif)==abs(numberDif):
            printStr+=' '
            printStr+=letterList[letterIndex]
            printStr+=' '
            printStr+=str(numberList[numberIndex])
            count+=1

    if letterIndex>tLetterIndex:
        letterSign=-1
    else:
        letterSign=1
    if numberIndex>tNumberIndex:
        numberSign=-1
    else:
        numberSign=1
        
    while letterDif!=0:
        letterIndex+=letterSign
        numberIndex+=numberSign
    
        letterDif=letterIndex-tLetterIndex
        numberDif=numberIndex-tNumberIndex
        
        if letterDif==0:
            printStr+=' '
            printStr+=letterList[letterIndex]
            printStr+=' '
            printStr+=str(numberList[numberIndex])
            count+=1
    

    return str(count)+printStr
printList=[]
index=0
for i in sys.stdin:
    n=int(i.split()[0])
    break;
for i in sys.stdin:
    
    ab=i.split()
    sLetter=str(ab[0])
    sNumber=int(ab[1])
    fLetter=str(ab[2])
    fNumber=int(ab[3])
    printList.append(printForOneLine(sLetter, sNumber, fLetter, fNumber))
    index+=1
    if index==n:
        break;
for item in printList:
    print(item)
