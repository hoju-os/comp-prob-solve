decimalNum = 255
baseNum = 2
quotient = 1
answer = ""
remainder = 0
while(quotient != 0):
    quotient = int (decimalNum/baseNum)
    remainder = decimalNum%baseNum
    answer = str(remainder)+ str(answer)
    decimalNum = quotient
print(answer)
    
