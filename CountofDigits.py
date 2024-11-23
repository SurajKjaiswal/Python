n=int(input("Enter the Digit: "))
c=0
while(n!=0):
    r=n%10
    c=c+1
    n=n//10
print("Count of the Digit is : ",c)

'''
Enter the Digit: 97766543
Count of the Digit is :  8

'''
