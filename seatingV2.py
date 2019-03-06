print("1 - Find a student's name by entering a row and seat")
print("2 - Find a student's row and seat by entering their name")
print ("3 - Find all student's in a row by entering a row")
print ("4 - Find all student's sitting in a seat across all rows by entering a seat")
print("E - End the program")

HaveMenu = False

while HaveMenu == False:
    try:
        num = input("Enter a menu item: ")
        if(num =="1" or num=="2" or num=="3" or num=="4" or num=="E"):
            HaveMenu = True
        
    except:
        print ('please re-enter...')

#Array of names
names=[["joe","bill","tom","zeke"],["anne","kate","sally","joan"],["stu1","stu2","stu3","stu4"]]


#This is a nested loop on row and seat within a row using a range which gives us access to the row and seat index 
if num == "1":
    row =int(input("Enter the row: "))
    seat =int(input("Enter the seat: "))
    print(names[row-1][seat-1])

    #The student sitting in row <row> seat <seat> is <name>


if num == "2":
    searchname=input("Enter a name to find: ")
    for row in range (0,len(names)):
        for seat in range (0,len(names[row])):
            if names[row][seat]==searchname:
                print (searchname + " is in row " + str(row+1) + " seat " + str(seat+1))
    print("name not found")            

if num == "3":
    print("menu item 3")
    row =int(input("Enter the row: "))
    for x in names[row-1]:
        print(x , end=" ")
    #put code here

if num == "4":
    print("menu item 4")

    seatSearch = int(input("Enter the seat: "))
    seatSearch = seatSearch - 1
    for row in range (0,len(names)):
        for seat in range (0,len(names[row])):
            if seat == seatSearch:
                print(names[row][seat])
    #put code here

if num =="E":
    print("Goodbye")
