

# if_else
n=int(input("Enter a Number:"))
if(n==0):
    print("You have entered zero")
else:
    print("You have entered :",n)

# if_elif_else
p=int(input("Enter the Number:"))

if(p>0):
     print("Number is Positive")
elif(p<0):
    print("Number is Negative")
else:
    print("Entered Number is zero")

#  Write a program to calculate greatest of three numbers.

# Nested if_else
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))

if(x>y):
    if(x>z):
        print("x is Greater")
    else:
        print("z is Greater")
else:
    if(y>z):
        print("y is Greater")
    else:
        print("z is Greater")

#<-------------- Output ---------------->

        '''
Enter First Number:4
Enter Second Number:5
Enter Third Number:6
z is Greater
'''
     

    
        
      



