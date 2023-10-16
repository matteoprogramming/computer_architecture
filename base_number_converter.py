def convertToBaseTen(number, base):
    numberString = str(number)
    base = int(base)
    baseTenNumber = 0
    i = 0
    while i<len(numberString):
        baseTenNumber += (int("0123456789ABCDEF".find(numberString[len(numberString)-1-i]))) * (base**i)
        i += 1
    return baseTenNumber


def converToGenericBase(n, base):
    n = int(n)
    base = int(base)
    if n == 0:
        return 0
    else:
        numberString=""
        while n!=0:
            numberString = str("0123456789ABCDEF"[(n % base)]) + numberString
            n = n//base
        return numberString
    
    
def printAllBases(number, base):
    n = convertToBaseTen(number, base)
    for i in range(2,17):
        a = converToGenericBase(n,i)
        if i<10:
            i_st = str(i)+" "
        else:
            i_st = str(i)
        print ("Base ",i_st," --> ",a)

def convertFromABaseToAnother(number,initialBase, finalBase):
    if check(number, initialBase):
        baseTenNumber = convertToBaseTen(number, initialBase)
        finalNumber = converToGenericBase(baseTenNumber, finalBase)
        return finalNumber
    else:
        print("Error")


def check(number, base):
    numberString = str(number)
    baseString = str(base)
    if numberString == "" or baseString == "":
        return False
    for i in numberString:
        if not(i in "0123456789ABCDEF"):
            return False
    for i in baseString:
        if not(i  in "0123456789"):
            return False
    if int(baseString)==0 or int(baseString)==1:
        return False
    for i in numberString:
        if int("0123456789ABCDEF".find(i))>= int(baseString):
             return False
    return True

if __name__ == "__main__":
    numberString = str(input("Enter the number you want to convert: "))
    baseString = str(input("Enter the base of the number entered: "))
    if check(numberString, baseString):
        base = int(baseString)
        printAllBases(numberString,baseString)
    else:
        print("Error")
