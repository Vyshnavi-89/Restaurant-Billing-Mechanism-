import time as s
from datetime import datetime
ft = datetime.now().strftime("%d/%m/%Y")
dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
sum=0
f = open("BILLDETAILS.txt", "a")
f.write(ft)
f.write("\n")
f.write("\nGetting Business Back")
f.write("\n")
while(1):
    print()
    print("********************************")
    print("Welcome to the Restaurant")
    k={1:"idli - 30 INR",2:"dosa - 45 INR",3:"coffee - 15 INR",4:"tea - 10 INR",5:"pizza - 60 INR",6:"sandwich - 50 INR",7:"burger - 100 INR"}
    for i in k:
        print(i,":",k[i])
    n=int(input("Enter the number of items required\n"))
    print("Select the required items from the above list and enter the number")
    o=[]
    for i in range(0,n):
        ind=input()
        if not ind.isdigit():
            print("Invalid Input, Insert the Sl.no against your choice ")
            f.write("*\*\*\*\*\*\*\ EXITED HERE DUE TO WRONG I/O /*/*/*/*/*/*/*/*/*\n")
            exit()
        ind=int(ind)
        if ind>7 or ind<1:
            print("choose an item from the given list only")
            ind=int(input())
            if ind>7 or ind<1:
                            print("You have chose the invalid item")
                            print("Please call for assistance")
                            print("**********************************")
                            f.write("*\*2\*\*\*\*\*\EXITED HERE/*/*/*/*/*/*/*/*/*\n")
                            exit()
        else:
             o.append(ind)
             print("You have selected", k[ind].strip("- INR0123456789"))
    print("Processing the order\n")
    for i in range(4):
        print("..",end="")
        s.sleep(0.5)
    print("Collect your order and Bill")
    print("\n******BILL RECEIPT******")
    print(dt)
    print("Items: ")
    for i in range(0,n):
        ind=o[i]
        print(i+1,".",k[ind].strip("- INR0123456789\n"))
    ta=0
    for i in range(0,n):
        ind=o[i]
        ta=ta+int(k[ind].strip("- INR abcdefghijklmnopqrstuvwxyz"))
    print("Total Amount: ",ta)
    f = open("BILLDETAILS.txt", "a")
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f.write(dt)
    f.write("\n")
    for i in range(0,n):
        ind=o[i]
        f.write(k[ind])
        f.write(",")
    f.write("\nAmount:")
    f.write(str(ta))
    sum=sum+ta
    f.write("\nTotal Cash in:")
    f.write(str(sum))
    f.write("\n")
    f.write("====================\n")
    print("       THANK YOU")
    print("****** VISIT AGAIN ********")
    s.sleep(0.9)
    f.close()