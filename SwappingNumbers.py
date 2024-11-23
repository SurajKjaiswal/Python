# Using input function take two number and then swap the number

a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))

print("Before Swapping: a=",a,"and b=",b)
# Swapping By Using 's' As Third Variable
s=a
a=b
b=s

print("After Swapping: a=",a,"and b=",b)

'''
Enter the first value:10
Enter the second value:20
Before Swapping: a= 10 and b= 20
After Swapping: a= 20 and b= 10
'''


# Swapping Without Using Third Variable
a=a+b
b=a-b
a=a-b
print("Double Swapping: a=",a,"and b=",b)

# Easy way in Python to swap Numbers 

a,b=b,a
print("Easy Way for Swapping: a=",a,"and b=",b)

'''
Before Swapping: a= 10 and b= 20
After Swapping: a= 20 and b= 10
Double Swapping: a= 10 and b= 20
Easy Way for Swapping: a= 20 and b= 10

'''
