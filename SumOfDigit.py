n=int(input("Enter the Digit: "))
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print("Sum of the Digit is : ",s)

#,------- Output ------->
'''
Enter the Digit: 123456
Sum of the Digit is :  6

'''
