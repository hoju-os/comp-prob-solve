try:
    while True:
        decimalNum = input('Enter a decimal number: ')
        baseNum = input('Enter a new base number: ')
        quotient = 1
        answer = ""
        if(baseNum == 2):
            while(quotient != 0):
                quotient = int (decimalNum/baseNum)
                remainder = decimalNum%baseNum
                answer = str(remainder)+ str(answer)
                decimalNum = quotient
        else:
            while(quotient != 0):
                quotient = int (decimalNum/baseNum)
                remainder = decimalNum%baseNum
                if(remainder == 10):
                    remainder = 'A'
                if(remainder == 11):
                    remainder = 'B'
                if(remainder == 12):
                    remainder = 'C'
                if(remainder == 13):
                    remainder = 'D'
                if(remainder == 14):
                    remainder = 'E'
                if(remainder == 15):
                    remainder = 'F'
                answer = str(remainder)+ str(answer)
                decimalNum = quotient
        print(answer)
except KeyboardInterrupt:
    pass
