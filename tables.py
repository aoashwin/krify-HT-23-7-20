n= int (input("Enter the number to print the tables for:"))
m= int (input("enter the number"))
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,"x",j,"=",i*j)
    print('\n')
